"""docs/checks.md: what ApiChecks found about the behaviour testers reported, as plain answers.

Each answer says what was seen and how often, or "not seen yet" with what to do in game to get it.
"""

import os


def _d(x):
    """A table the Lua parser may have turned into a dict or a list."""
    if isinstance(x, list):
        return {str(i + 1): v for i, v in enumerate(x)}
    return x or {}


def _l(x):
    if isinstance(x, dict):
        return [x[k] for k in sorted(x, key=lambda k: int(k) if str(k).isdigit() else 0)]
    return x or []


def answers(c):
    """[(question, answer, evidence lines)] from an ApiChecks import."""
    out = []
    if not c:
        return out
    tw = _d(c.get("twice"))
    for ev, what in (("PLAYER_DEAD", "a death"), ("MERCHANT_CLOSED", "closing a vendor"),
                     ("AUCTION_HOUSE_CLOSED", "closing the auction house")):
        r = _d(tw.get(ev))
        fires = _d(r.get("fires"))
        n = sum(fires.values()) if fires else 0
        if not n:
            out.append(("Does %s fire twice?" % ev, "Not seen yet: needs %s." % what, []))
            continue
        twice = sum(v for k, v in fires.items() if str(k) != "1")
        ans = ("**Yes**: %d of %d times it fired more than once." % (twice, n)) if twice else ("**No**: once each time (%d seen)." % n)
        gaps = [e.get("gapMs") for e in _l(r.get("recent")) if (e.get("fires") or 1) > 1]
        ev_lines = ["fires per %s: %s" % (what, ", ".join("%s× %s" % (k, v) for k, v in sorted(fires.items())))]
        if gaps:
            ev_lines.append("gap between the copies: up to %d ms" % max(g or 0 for g in gaps))
        out.append(("Does %s fire twice?" % ev, ans, ev_lines))

    z = _d(c.get("zone"))
    tally = _d(z.get("tally"))
    for ev in ("PLAYER_ENTERING_WORLD", "ZONE_CHANGED_NEW_AREA"):
        rows = {k: v for k, v in tally.items() if k.startswith(ev)}
        q = "Is the zone text stale at %s?" % ev
        if not rows:
            out.append((q, "Not seen yet: needs a zone change.", []))
            continue
        lines = ["%s: stale %d of %d" % (k.split(" / ", 1)[1], v.get("stale", 0), v.get("n", 0)) for k, v in sorted(rows.items())]
        stale = sum(v.get("stale", 0) for v in rows.values())
        ans = ("**Yes, sometimes**: the text changed within 3 s of the event %d times. Read it again a moment later "
               "(or on ZONE_CHANGED / the next frame)." % stale) if stale else "**No**: the text was already right when the event fired."
        missing = [h for h in ("spell", "taxi", "loading screen") if not any(h in k for k in rows)]
        if missing:
            ans += " Not covered yet: arriving by %s." % ", ".join("hearth or portal" if h == "spell" else h for h in missing)
        out.append((q, ans, lines))

    ch = _d(c.get("chat"))
    trig, msgs = _d(ch.get("triggers")), _d(ch.get("messages"))
    for key, label in (("rested", '"You feel rested."'), ("auction", '"Auction created."'), ("afkOff", "AFK off"),
                       ("afkOn", "AFK on")):
        q = "Does %s skip the CHAT_MSG_ events?" % label
        n = trig.get(key, 0)
        seen = _d(msgs.get(key))
        if not n and not seen:
            out.append((q, "Not seen yet.", []))
            continue
        lines = ["triggered %d times" % n] + ["seen on %s: %d" % (k, v) for k, v in sorted(seen.items())]
        if seen.get("CHAT_MSG_SYSTEM"):
            ans = "**No**: it arrives as CHAT_MSG_SYSTEM."
        elif seen.get("UI_INFO_MESSAGE") or seen.get("UI_ERROR_MESSAGE"):
            ans = "**Yes**: it comes as %s instead." % " / ".join(k for k in ("UI_INFO_MESSAGE", "UI_ERROR_MESSAGE") if seen.get(k))
        elif seen.get("chat frame"):
            ans = "**Yes**: the UI prints it to the chat frame without any event an add-on can catch."
        else:
            ans = "**Yes**: not seen on CHAT_MSG_SYSTEM, UI_INFO_MESSAGE or in the chat frame."
        out.append((q, ans, lines))
    sec = _d(ch.get("secretOn"))
    if sec:
        out.append(("Are system messages ever secret?", "**Yes**: some couldn't be compared because the text was secret.",
                    ["%s: %d" % kv for kv in sorted(sec.items())]))

    p = _d(c.get("project"))
    if p:
        out.append(("Does WOW_PROJECT_ID report 1 (Retail)?",
                    "**No**: it is %s. WOW_PROJECT_MAINLINE is %s, WOW_PROJECT_CLASSIC %s, WOW_PROJECT_CAMELOT %s." %
                    (p.get("id"), p.get("mainline"), p.get("classic"), p.get("camelot")), []))

    send = _d(c.get("send"))
    runs = {k: v for k, v in send.items() if isinstance(v, dict) and v.get("results")}
    if not runs:
        out.append(("Can add-ons say, yell or emote in instances?", "Not tested yet: run /apichecks chat in the world and in a dungeon.", []))
    for where, run in sorted(runs.items()):
        lines = []
        for k, r in sorted(_d(run.get("results")).items()):
            echo = r.get("echo")
            lines.append("%s: %s%s" % (k, r.get("sent"), "" if echo is None else (", came back" if echo else ", never came back")))
        ok = [k for k, r in _d(run.get("results")).items() if r.get("sent") == "ok" and r.get("echo") is not False]
        out.append(("Can add-ons say, yell or emote (%s)?" % where,
                    ("Went through: %s." % ", ".join(sorted(ok))) if ok else "**Nothing went through.**", lines))

    fd = _d(c.get("feed"))
    for ev in ("UNIT_COMBAT", "COMBAT_LOG_MESSAGE", "COMBAT_TEXT_UPDATE", "DAMAGE_METER_COMBAT_SESSION_UPDATED"):
        r = _d(fd.get(ev))
        if not r:
            out.append(("What does %s carry?" % ev, "Not seen yet.", []))
            continue
        sigs, ph = _d(r.get("sigs")), _d(r.get("phases"))
        secret = any(any(ch.isupper() for ch in s) for s in sigs)
        lines = ["arguments: %s (capitals are secret)" % ", ".join("%s ×%d" % kv for kv in sorted(sigs.items(), key=lambda kv: -kv[1])),
                 "when: %s" % ", ".join("%s ×%d" % kv for kv in sorted(ph.items()))]
        for k, label in (("actions", "actions"), ("units", "units"), ("types", "types"), ("info", "GetCurrentCombatTextEventInfo")):
            if r.get(k):
                lines.append("%s: %s" % (label, ", ".join("%s ×%d" % kv for kv in sorted(_d(r[k]).items(), key=lambda kv: -kv[1])[:15])))
        if r.get("readable"):
            lines.append("readable lines: %d, wrapped in |K...|k: %d" % (r["readable"], r.get("wrapped", 0)))
        ans = "Fires %s; %s." % ("in combat too" if ph.get("combat") else "only out of combat so far",
                                 "some arguments are secret" if secret else "no secret arguments seen")
        out.append(("What does %s carry?" % ev, ans, lines))
    m = _d(c.get("meter"))
    if m:
        lines = []
        for label in ("outside", "combat", "after combat"):
            snap = _d(m.get(label))
            if snap:
                lines.append("**%s**" % label)
                lines += ["%s → %s" % (k, v) for k, v in sorted(snap.items())
                          if k not in ("at", "combat", "done", "types", "sessionTypes")]
        out.append(("What does C_DamageMeter give add-ons?", "Shapes below; *secret* marks a secret value.", lines))

    s = _d(c.get("secrets"))
    for key, q in (("spellcastSent", "Is UNIT_SPELLCAST_SENT's target secret?"),
                   ("unitIsUnit", "Does UnitIsUnit return a secret against enemy units?"),
                   ("pet", 'Is UnitHealth("pet") secret?')):
        r = _d(s.get(key))
        if not r:
            out.append((q, "Not seen yet.", []))
            continue
        lines = ["%s: %s" % (k, ", ".join("%s ×%d" % kv for kv in sorted(_d(v).items()))) for k, v in sorted(r.items())]
        any_secret = any("secret" in str(k) and "plain" not in str(k) for v in r.values() for k in _d(v))
        out.append((q, "**Yes, in the cases below.**" if any_secret else "**No secret seen.**", lines))
    return out


def render_md(checks, path):
    lines = ["# Reported quirks, checked", "",
             "Behaviour testers reported on Forever, checked in game by the ApiChecks add-on. Each answer comes from "
             "what the add-on saw; \"not seen yet\" means it hasn't watched that happen.", ""]
    if not checks:
        lines += ["No ApiChecks data yet: enable the API checks add-on, play, then run update-docs.bat.", ""]
    else:
        lines += ["Client %s, add-on %s." % (checks.get("build"), checks.get("probe")), ""]
        for q, a, ev in answers(checks):
            lines += ["## " + q, "", a, ""]
            lines += ["- " + e for e in ev]
            lines.append("")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
