"""Read Lua table literals: Blizzard's generated API docs and WoW SavedVariables files.

Only data is parsed, never run. Anything that isn't a literal (Blizzard's docs use expressions such as
`Constants.X.Y * 2` or `MAX_RAID_MARKERS`) comes back as an Expr holding its source text.
"""

import re


class Expr(str):
    """Source text of a value that isn't a literal."""


class LuaSyntaxError(ValueError):
    pass


_NUM = re.compile(r"-?(0[xX][0-9a-fA-F]+|(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?)")
_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_ESC = {"n": "\n", "t": "\t", "r": "\r", "a": "\a", "b": "\b", "f": "\f", "v": "\v",
        "\\": "\\", '"': '"', "'": "'", "\n": "\n"}


class Parser:
    def __init__(self, text):
        self.s = text
        self.i = 0

    def error(self, msg):
        line = self.s.count("\n", 0, self.i) + 1
        raise LuaSyntaxError("%s at line %d" % (msg, line))

    def skip(self):
        s, n = self.s, len(self.s)
        while self.i < n:
            c = s[self.i]
            if c in " \t\r\n;":
                self.i += 1
            elif s.startswith("--", self.i):
                m = re.match(r"--\[(=*)\[", s[self.i:self.i + 20])
                if m:
                    end = s.find("]" + m.group(1) + "]", self.i)
                    self.i = n if end < 0 else end + len(m.group(1)) + 2
                else:
                    end = s.find("\n", self.i)
                    self.i = n if end < 0 else end + 1
            else:
                break

    def peek(self):
        self.skip()
        return self.s[self.i] if self.i < len(self.s) else ""

    def string(self):
        s, q = self.s, self.s[self.i]
        if q == "[":
            m = re.match(r"\[(=*)\[", s[self.i:])
            close = "]" + m.group(1) + "]"
            start = self.i + len(m.group(0))
            end = s.find(close, start)
            if end < 0:
                self.error("unfinished long string")
            self.i = end + len(close)
            body = s[start:end]
            return body[1:] if body.startswith("\n") else body
        self.i += 1
        out = []
        while True:
            j = self.i
            while j < len(s) and s[j] not in (q, "\\"):
                j += 1
            out.append(s[self.i:j])
            if j >= len(s):
                self.error("unfinished string")
            if s[j] == q:
                self.i = j + 1
                return "".join(out)
            e = s[j + 1]
            if e.isdigit():
                m = re.match(r"\d{1,3}", s[j + 1:])
                out.append(chr(int(m.group(0))))
                self.i = j + 1 + len(m.group(0))
            elif e in _ESC:
                out.append(_ESC[e])
                self.i = j + 2
            elif e == "\r":
                out.append("\n")
                self.i = j + 3 if s[j + 2:j + 3] == "\n" else j + 2
            else:
                out.append(e)
                self.i = j + 2

    def raw_expr(self):
        """Source text up to the next , ; or } at this depth."""
        s, depth, start = self.s, 0, self.i
        while self.i < len(s):
            c = s[self.i]
            if c in "\"'":
                self.string()
                continue
            if c in "({[":
                depth += 1
            elif c in ")]}":
                if depth == 0:
                    break
                depth -= 1
            elif c in ",;" and depth == 0:
                break
            self.i += 1
        return Expr(s[start:self.i].strip())

    def value(self):
        c = self.peek()
        if c == "{":
            return self.table()
        if c in "\"'" or self.s.startswith("[[", self.i) or self.s.startswith("[=", self.i):
            v = self.string()
            return v if self.peek() in ",;}]" else Expr(repr(v) + self.raw_expr())
        start = self.i
        m = _NUM.match(self.s, self.i)
        if m:
            self.i = m.end()
            if self.peek() in ",;}]" or self.peek() == "":
                t = m.group(0)
                if "x" in t or "X" in t:
                    return int(t, 16)
                return float(t) if any(ch in t for ch in ".eE") else int(t)
            self.i = start
            return self.raw_expr()
        m = _NAME.match(self.s, self.i)
        if m:
            word = m.group(0)
            self.i = m.end()
            if self.peek() in ",;}]" or self.peek() == "":
                if word in ("true", "false"):
                    return word == "true"
                if word == "nil":
                    return None
            self.i = start
            return self.raw_expr()
        return self.raw_expr()

    def table(self):
        self.i += 1  # {
        arr, rec = [], {}
        while True:
            c = self.peek()
            if c == "}":
                self.i += 1
                break
            if c == "":
                self.error("unfinished table")
            if c == "[" and not (self.s.startswith("[[", self.i) or self.s.startswith("[=", self.i)):
                self.i += 1
                key = self.value()
                if self.peek() != "]":
                    self.error("expected ]")
                self.i += 1
                if self.peek() != "=":
                    self.error("expected =")
                self.i += 1
                rec[key] = self.value()
            else:
                m = _NAME.match(self.s, self.i)
                save = self.i
                if m:
                    self.i = m.end()
                    if self.peek() == "=" and not self.s.startswith("==", self.i):
                        self.i += 1
                        rec[m.group(0)] = self.value()
                        self.after_field()
                        continue
                    self.i = save
                arr.append(self.value())
            self.after_field()
        if not rec:
            return arr
        for n, v in enumerate(arr, 1):
            rec[n] = v
        return rec

    def after_field(self):
        c = self.peek()
        if c in ",;":
            self.i += 1


def parse_value(text):
    return Parser(text).value()


def parse_assignments(text):
    """Top-level `Name = value` statements (SavedVariables files, `local X = {...}` doc files)."""
    p, out = Parser(text), {}
    while True:
        p.skip()
        if p.i >= len(p.s):
            return out
        m = re.compile(r"(?:local\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*").match(p.s, p.i)
        if not m:
            # a statement we don't read (APIDocumentation:AddDocumentationTable(X)); skip the line
            end = p.s.find("\n", p.i)
            p.i = len(p.s) if end < 0 else end + 1
            continue
        p.i = m.end()
        out[m.group(1)] = p.value()
