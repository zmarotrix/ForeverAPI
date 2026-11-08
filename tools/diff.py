"""Compare two dumps (or two client-doc extracts): what a client patch added, removed or changed."""

import os
from collections import defaultdict


def flatten(data):
    """Path -> short value for everything a patch could change. Works for dumps and client-doc extracts."""
    out = {}
    if "systems" in data:  # client docs extract
        for s in data["systems"]:
            ns = s.get("Namespace")
            for kind in ("Functions", "Events", "Tables"):
                items = s.get(kind) or []
                if isinstance(items, dict):
                    items = list(items.values())
                for it in items:
                    if not isinstance(it, dict):
                        continue
                    name = it.get("LiteralName") or it.get("Name")
                    key = "%s/%s" % (kind.lower(), ((ns + ".") if ns and kind == "Functions" else "") + str(name))
                    out[key] = _short({k: v for k, v in it.items() if k != "Documentation"})
        return out
    for name, code in (data.get("globals") or {}).items():
        out["globals/" + name] = code
    for tname, members in (data.get("tables") or {}).items():
        if isinstance(members, dict):
            for k, v in members.items():
                out["tables/%s.%s" % (tname, k)] = _short(v)
    for w, rec in (data.get("widgets") or {}).items():
        if rec.get("error"):
            out["widgets/%s" % w] = "error: " + str(rec["error"])
        for m, c in (rec.get("methods") or {}).items():
            out["widgets/%s:%s" % (w, m)] = c
        out["widgets/%s (scripts)" % w] = ",".join(sorted(map(str, _vals(rec.get("scripts")))))
    for e, rec in (data.get("events") or {}).items():
        out["events/" + e] = rec.get("register") if isinstance(rec, dict) else rec
    for c, rec in (data.get("cvars") or {}).items():
        out["cvars/" + str(c)] = (rec or {}).get("default") if isinstance(rec, dict) else rec
    for phase in ("outside", "combat"):
        for k, rec in ((data.get("calls") or {}).get(phase) or {}).get("results", {}).items():
            out["calls-%s/%s" % (phase, k)] = _short({x: y for x, y in rec.items() if x not in ("from", "arg")})
    return out


def _vals(v):
    if isinstance(v, dict):
        return list(v.values())
    return v or []


def _short(v):
    s = repr(v)
    return s if len(s) <= 300 else s[:300] + "..."


def write_report(a, b, name_a, name_b, out):
    fa, fb = flatten(a), flatten(b)
    groups = defaultdict(lambda: {"added": [], "removed": [], "changed": []})
    for k in sorted(set(fa) | set(fb)):
        g = k.split("/", 1)[0]
        if k not in fa:
            groups[g]["added"].append((k, None, fb[k]))
        elif k not in fb:
            groups[g]["removed"].append((k, fa[k], None))
        elif fa[k] != fb[k]:
            groups[g]["changed"].append((k, fa[k], fb[k]))
    lines = ["# Changes", "", "From `%s`" % os.path.basename(name_a), "to `%s`" % os.path.basename(name_b), ""]
    ma, mb = a.get("meta") or {}, b.get("meta") or {}
    if ma or mb:
        lines += ["Builds: %s → %s" % (ma.get("key", a.get("version")), mb.get("key", b.get("version"))), ""]
    if not groups:
        lines.append("No differences.")
    for g, ch in sorted(groups.items()):
        lines += ["## %s" % g, "", "%d added, %d removed, %d changed" % tuple(len(ch[x]) for x in ("added", "removed", "changed")), ""]
        for kind in ("added", "removed", "changed"):
            if not ch[kind]:
                continue
            lines += ["### %s" % kind.capitalize(), ""]
            for k, old, new in ch[kind][:2000]:
                path = k.split("/", 1)[1]
                if kind == "changed":
                    lines.append("- `%s`: `%s` → `%s`" % (path, old, new))
                else:
                    lines.append("- `%s`: `%s`" % (path, new if kind == "added" else old))
            if len(ch[kind]) > 2000:
                lines.append("- ...and %d more" % (len(ch[kind]) - 2000))
            lines.append("")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
