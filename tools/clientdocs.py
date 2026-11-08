"""Pull Blizzard's generated API docs and FrameXML leads out of the installed client.

The Forever client ships Blizzard_APIDocumentationGenerated (one Lua table per API system). Those files are what
Blizzard's build thinks the API is; they are leads, not proof, until the in-game probe confirms them.
Read through the suite's read-only CASC reader (pfQuest-Forever/tools/oracle_maps/casc.py).
"""

import os
import re
import sys

from luatable import parse_assignments

SUITE_CASC = r"G:\Projects\pfQuest\pfQuest-Forever\tools\oracle_maps"
GEN = "Interface/AddOns/Blizzard_APIDocumentationGenerated/"


def _casc():
    if SUITE_CASC not in sys.path:
        sys.path.insert(0, SUITE_CASC)
    import casc  # noqa: E402
    return casc


def _toc_files(c, folder):
    raw = c.read_path(folder + os.path.basename(folder.rstrip("/")) + ".toc")
    if raw is None:
        return []
    out = []
    for line in raw.decode("utf-8", "replace").splitlines():
        line = line.split("[")[0].strip()
        if line and not line.startswith("#") and line.endswith((".lua", ".xml")):
            out.append(line.replace("\\", "/"))
    return out


def extract():
    """{"version", "systems": [...]} from the client's generated docs."""
    casc = _casc()
    c = casc.CASC()
    _, version = casc.active_build()
    systems = []
    for name in _toc_files(c, GEN):
        raw = c.read_path(GEN + name)
        if raw is None:
            continue
        for var, value in parse_assignments(raw.decode("utf-8", "replace")).items():
            # systems have a Name; constants-only files are a bare { Tables = {...} } named by their local
            if isinstance(value, dict) and ("Name" in value or "Tables" in value):
                value.setdefault("Name", var)
                value.setdefault("Type", "Tables")
                value["File"] = name
                systems.append(value)
    return {"version": version, "systems": systems}


# FrameXML leads: names the client's own UI code uses that the generated docs may not list (legacy globals,
# events without docs). The probe checks each one before it's documented.
_EVENT_RE = re.compile(r"""(?:Register(?:Unit)?Event|RegisterEventCallback|FrameUtil\.RegisterFrameForEvents)\(\s*(?:self\s*,\s*)?["']([A-Z][A-Z0-9_]+)["']""")
_EVENT_LIST_RE = re.compile(r"""^\s*["']([A-Z][A-Z0-9_]{4,})["'],\s*$""", re.M)
_CALL_RE = re.compile(r"(?<![\w.:])([A-Z][A-Za-z0-9]+)\s*\(")
_DEF_RE = re.compile(r"^\s*function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(|^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*function", re.M)


def framexml_leads():
    """{"events", "globals" (called), "defined" (global functions written in Lua)}: name -> first UI file."""
    casc = _casc()
    c = casc.CASC()
    raw = c.read_path("Interface/ui-code-list.txt")
    events, calls, defined = {}, {}, {}
    if raw is None:
        return {"events": events, "globals": calls, "defined": defined}
    for path in raw.decode("utf-8", "replace").splitlines():
        path = path.strip().replace("\\", "/")
        if not path.endswith(".lua") or GEN in path:
            continue
        data = c.read_path(path)
        if data is None:
            continue
        text = data.decode("utf-8", "replace")
        short = path[len("Interface/AddOns/"):] if path.startswith("Interface/AddOns/") else path
        for name in _EVENT_RE.findall(text) + _EVENT_LIST_RE.findall(text):
            events.setdefault(name, short)
        for name in _CALL_RE.findall(text):
            calls.setdefault(name, short)
        for a, b in _DEF_RE.findall(text):
            defined.setdefault(a or b, short)
    return {"events": events, "globals": calls, "defined": defined}
