/* Forever API docs: a static, hash-routed page over window.API (written by tools/site.py). */
(function () {
  "use strict";
  var A = window.API;
  var main = document.getElementById("main");
  var STATUS = {
    "verified": ["✓", "verified", "Confirmed in game"],
    "undocumented": ["＋", "game only", "In game, not in Blizzard's docs (Forever-only or legacy)"],
    "not-in-game": ["✕", "not in game", "In Blizzard's docs, not in this client"],
    "unverified": ["?", "unverified", "Not checked in game yet"]
  };
  var FN_KIND = { fC: "built-in", fL: "Lua", "f?": "function" };
  var FLAG_WORDS = {
    IsProtectedFunction: "protected", HasRestrictions: "restricted in some situations",
    SecretReturns: "always secret", SecretWhenInCombat: "secret in combat",
    SecretWhenUnitAuraRestricted: "secret while auras restricted", SecretWhenUnitStatsRestricted: "secret while stats restricted",
    SecretWhenUnitIdentityRestricted: "secret while identity restricted", SecretWhenUnitSpellCastRestricted: "secret while casts restricted",
    SecretWhenUnitPowerRestricted: "secret while power restricted", SecretWhenCooldownsRestricted: "secret while cooldowns restricted",
    SecretInChatMessagingLockdown: "secret in chat lockdown", ConditionalSecret: "secret in some conditions",
    ReturnsNeverSecret: "never secret", SynchronousEvent: "synchronous", UniqueEvent: "unique", MayReturnNothing: "may return nothing"
  };

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function enc(s) { return encodeURIComponent(s); }
  function pill(status) { var s = STATUS[status] || STATUS.unverified; return '<span class="pill s-' + esc(status) + '" title="' + esc(s[2]) + '">' + s[0] + " " + s[1] + "</span>"; }
  function keys(o) { return Object.keys(o || {}); }
  function sortStr(a, b) { a = a.toLowerCase(); b = b.toLowerCase(); return a < b ? -1 : a > b ? 1 : 0; }

  // ---------------------------------------------------------------- indexes
  var pages = {};   // page name -> { ns, fns:[], events:[], types:[] }
  var nsPage = {};
  function page(name) { return pages[name] || (pages[name] = { ns: null, fns: [], events: [], types: [] }); }
  keys(A.F).forEach(function (k) { var f = A.F[k]; if (f.sys && f.ns && !nsPage[f.ns]) nsPage[f.ns] = f.sys; });
  keys(A.F).forEach(function (k) {
    var f = A.F[k]; f.key = k;
    var p = f.sys || (f.ns ? (nsPage[f.ns] || f.ns) : null);
    f.page = p;
    if (p) { var pg = page(p); pg.fns.push(k); if (f.ns) pg.ns = pg.ns || f.ns; }
  });
  keys(A.E).forEach(function (k) { var e = A.E[k]; if (e.sys) page(e.sys).events.push(k); });
  keys(A.T).forEach(function (k) { var t = A.T[k]; if (t.sys) page(t.sys).types.push(k); });
  var pageNames = keys(pages).sort(sortStr);

  function count(list, getter) {
    var c = { verified: 0, undocumented: 0, "not-in-game": 0, unverified: 0 };
    list.forEach(function (x) { c[getter(x)] = (c[getter(x)] || 0) + 1; });
    return c;
  }

  // search index
  var SEARCH = [];
  keys(A.F).forEach(function (k) { var f = A.F[k]; SEARCH.push([k.toLowerCase(), "function", k, f.s, f.ui ? 1 : 0]); });
  keys(A.E).forEach(function (k) { SEARCH.push([k.toLowerCase(), "event", k, A.E[k].s, 0]); });
  keys(A.T).forEach(function (k) { var t = A.T[k]; SEARCH.push([k.toLowerCase(), t.k === "Enumeration" ? "enum" : t.k === "Constants" ? "constants" : "type", k, t.s || "", 0]); });
  keys(A.W).forEach(function (k) { SEARCH.push([k.toLowerCase(), "widget", k, A.W[k].err ? "not-in-game" : "verified", 0]); });
  keys(A.C).forEach(function (k) { SEARCH.push([k.toLowerCase(), "cvar", k, "verified", 1]); });
  pageNames.forEach(function (k) { SEARCH.push([k.toLowerCase(), "system", k, "", 0]); });
  function link(kind, key) {
    return { "function": "#/fn/", event: "#/event/", "enum": "#/type/", constants: "#/type/", type: "#/type/",
      widget: "#/widget/", cvar: "#/cvars/", system: "#/system/" }[kind] + enc(key);
  }

  // ---------------------------------------------------------------- pieces
  function typeLink(t) {
    var base = String(t).replace(/\[\]$/, "");
    var label = esc(t);
    return A.T[base] ? '<a class="t" href="#/type/' + enc(base) + '">' + label + "</a>" : '<span class="t">' + label + "</span>";
  }
  function params(list) {
    return (list || []).map(function (a) {
      var s = esc(a[0]) + ": " + typeLink(a[1]) + (a[2] ? "?" : "");
      if (a[3] != null) s += ' <span class="opt">= ' + esc(a[3]) + "</span>";
      return s;
    }).join(", ");
  }
  function signature(name, args, rets) {
    var s = esc(name) + "(" + params(args) + ")";
    if (rets && rets.length) s += "\n  → " + params(rets);
    return '<div class="sig">' + s + "</div>";
  }
  function flagPills(fl) {
    return keys(fl).filter(function (k) { return fl[k] !== false; }).sort().map(function (k) {
      var word = FLAG_WORDS[k] || (fl[k] === true ? k : k + ": " + fl[k]);
      if (k === "SecretArguments") word = "secret args: " + fl[k];
      var cls = /Secret/.test(k) && k !== "ReturnsNeverSecret" && k !== "SecretArguments" ? "p-secret" : /Protected|Restrict|Requires/.test(k) ? "p-warn" : "p-plain";
      return '<span class="pill ' + cls + '" title="' + esc(k) + ' (Blizzard\'s docs; not checked in game)">' + esc(word) + "</span>";
    }).join("");
  }
  function callCell(r, long) {
    if (!r) return '<span class="muted">—</span>';
    if (r.skipped) return '<span class="pill p-bad">' + esc(r.skipped) + "</span>";
    if (r.forbidden) return '<span class="pill p-bad">protected</span>';
    if (r.missing) return '<span class="pill p-bad">missing</span>';
    if (r.error != null) return long ? '<span class="err">' + esc(r.error) + "</span>" : '<span class="pill p-warn" title="' + esc(r.error) + '">error</span>';
    var rets = r.returns || [];
    if (!long) {
      var sec = rets.filter(function (v) { return /^secret/.test(v); }).length;
      if (rets.length && sec === rets.length) return '<span class="pill p-secret">secret</span>';
      if (sec) return '<span class="pill p-secret">partly secret</span>';
      return '<span class="muted">' + r.n + " value" + (r.n === 1 ? "" : "s") + "</span>";
    }
    if (!r.n) return '<span class="muted">returned nothing</span>';
    return '<span class="ret">' + rets.map(function (v) { return '<code class="' + (/^secret/.test(v) ? "sec" : "") + '">' + esc(v) + "</code>"; }).join("") + "</span>";
  }
  function same(a, b) { return JSON.stringify(a || null) === JSON.stringify(b || null); }

  function fnCard(k) {
    var f = A.F[k];
    var h = '<div class="card" id="' + esc(k) + '"><div class="head"><h3><a href="#/fn/' + enc(k) + '">' + esc(k) + "</a></h3>" + pill(f.s);
    if (f.g) h += '<span class="pill p-plain">' + esc(FN_KIND[f.g.split("!")[0]] || f.g) + "</span>";
    if (f.ui) h += '<span class="pill p-plain">Blizzard UI Lua</span>';
    h += "</div>";
    if (f.a || f.r) h += signature(k, f.a, f.r);
    if (f.d) h += "<p>" + esc(f.d) + "</p>";
    var docs = (f.a || []).concat(f.r || []).filter(function (a) { return a[4]; });
    var kv = "";
    docs.forEach(function (a) { kv += "<div><code>" + esc(a[0]) + "</code></div><div>" + esc(a[4]) + "</div>"; });
    if (f.fl) kv += "<div>Blizzard flags</div><div><div class=\"flags\">" + flagPills(f.fl) + '</div><div class="note">From the client docs; the call results below are what the game did.</div></div>';
    if (f.o) kv += "<div>Out of combat" + (f.o.arg === "unit" ? ' <span class="note">("player")</span>' : "") + "</div><div>" + callCell(f.o, true) + "</div>";
    if (f.c) kv += "<div>In combat</div><div>" + callCell(f.c, true) + (same(f.c.returns, f.o && f.o.returns) && !f.c.error === !(f.o && f.o.error) ? ' <span class="note">(same)</span>' : "") + "</div>";
    if (f.rep) kv += '<div>Warning</div><div><span class="pill p-warn">replaced by the add-on ' + esc(f.rep) + "</span></div>";
    if (f.w) kv += "<div>Web lead</div><div>" + esc(f.w.text || "") + ' <a href="' + esc(f.w.url || "#") + '">' + esc(f.w.site || "source") + '</a> <span class="note">(unverified)</span></div>';
    if (f.u) kv += "<div>Used by</div><div><code>" + esc(f.u) + "</code></div>";
    if (typeof f.ui === "string") kv += "<div>Defined in</div><div><code>" + esc(f.ui) + "</code></div>";
    if (f.page) kv += '<div>System</div><div><a href="#/system/' + enc(f.page) + '">' + esc(f.page) + "</a>" + (f.file ? ' <span class="note">' + esc(f.file) + "</span>" : "") + "</div>";
    if (kv) h += '<div class="kv">' + kv + "</div>";
    return h + "</div>";
  }

  function eventCard(k) {
    var e = A.E[k];
    var h = '<div class="card" id="' + esc(k) + '"><div class="head"><h3><a href="#/event/' + enc(k) + '">' + esc(k) + "</a></h3>" + pill(e.s);
    if (e.chk === "forbidden" || e.chk === "blocked") h += '<span class="pill p-bad">add-ons may not register</span>';
    h += "</div>";
    if (e.p) h += '<div class="sig">' + esc(k) + "(" + params(e.p) + ")</div>";
    else if (e.src === "client-docs") h += '<div class="sig">' + esc(k) + "()</div>";
    if (e.d) h += "<p>" + esc(e.d) + "</p>";
    var kv = "";
    if (e.fl) kv += "<div>Blizzard flags</div><div class=\"flags\">" + flagPills(e.fl) + "</div>";
    if (e.chk) kv += "<div>RegisterEvent</div><div><code>" + esc(e.chk) + "</code></div>";
    if (e.live) kv += "<div>Seen firing</div><div>" + e.live.n + " times, " + e.live.combat + " in combat · argument kinds " +
      keys(e.live.sigs).map(function (s) { return "<code>" + esc(s || "(none)") + "</code>"; }).join(" ") +
      ' <div class="note">n number, s string, b boolean, t table, S secret, - nil</div></div>';
    if (e.u) kv += "<div>Used by</div><div><code>" + esc(e.u) + "</code></div>";
    if (e.sys) kv += '<div>System</div><div><a href="#/system/' + enc(e.sys) + '">' + esc(e.sys) + "</a></div>";
    if (kv) h += '<div class="kv">' + kv + "</div>";
    return h + "</div>";
  }

  function typeCard(k) {
    var t = A.T[k];
    var h = '<div class="card" id="' + esc(k) + '"><div class="head"><h3><a href="#/type/' + enc(k) + '">' + esc(k) + '</a></h3><span class="pill p-plain">' + esc(t.k) + "</span>" + (t.s ? pill(t.s) : "") + "</div>";
    if (t.d) h += "<p>" + esc(t.d) + "</p>";
    var enumish = t.k === "Enumeration" || t.k === "Constants";
    if (t.f && t.f.length) {
      h += '<div class="tablewrap"><table><tr><th>Name</th><th>' + (enumish ? "Value" : "Type") + "</th>" + (enumish ? "" : "<th>Notes</th>") + "</tr>";
      t.f.forEach(function (x) {
        h += '<tr><td class="mono">' + esc(x[0]) + '</td><td class="mono">' + (enumish ? esc(x[3]) : typeLink(x[1]) + (x[2] ? "?" : "")) + "</td>" +
          (enumish ? "" : "<td>" + (x[4] != null ? "default <code>" + esc(x[4]) + "</code> " : "") + esc(x[5] || "") + "</td>") + "</tr>";
      });
      h += "</table></div>";
    }
    if (t.gv) {
      h += '<div class="tablewrap"><table><tr><th>Name</th><th>Value in game</th></tr>';
      t.gv.forEach(function (x) { h += '<tr><td class="mono">' + esc(x[0]) + '</td><td class="mono">' + esc(typeof x[1] === "object" ? JSON.stringify(x[1]) : x[1]) + "</td></tr>"; });
      h += "</table></div>";
    }
    (t.mm || []).forEach(function (m) { h += '<p><span class="pill p-warn">differs</span> <code>' + esc(m[0]) + "</code>: docs say " + esc(m[1]) + ", game has " + esc(m[2] == null ? "nothing" : String(m[2]).replace(/^n:/, "")) + "</p>"; });
    if (t.sys) h += '<div class="kv"><div>System</div><div><a href="#/system/' + enc(t.sys) + '">' + esc(t.sys) + "</a></div></div>";
    return h + "</div>";
  }

  // lists that can be long: render in slices
  function bigList(id, items, rowFn, header, step) {
    step = step || 300;
    var shown = 0;
    var holder = document.getElementById(id);
    function more() {
      var html = items.slice(shown, shown + step).map(rowFn).join("");
      shown += step;
      var tb = holder.querySelector("tbody");
      tb.insertAdjacentHTML("beforeend", html);
      var m = holder.querySelector(".more");
      m.innerHTML = shown < items.length ? "<button>Show more (" + (items.length - shown) + " left)</button>" : "";
      if (m.firstChild) m.firstChild.onclick = more;
    }
    holder.innerHTML = '<div class="tablewrap"><table><thead>' + header + "</thead><tbody></tbody></table></div><div class=\"more\"></div>" +
      (items.length ? "" : '<p class="muted">Nothing matches.</p>');
    more();
  }

  function filterBar(id, opts) {
    var h = '<div class="toolbar" id="' + id + '"><input type="search" placeholder="Filter by name" spellcheck="false">';
    (opts || []).forEach(function (o) { h += '<button class="chip" data-v="' + esc(o[0]) + '">' + esc(o[1]) + "</button>"; });
    return h + "</div>";
  }
  function wireFilter(id, onChange) {
    var bar = document.getElementById(id), input = bar.querySelector("input"), active = null;
    bar.querySelectorAll(".chip").forEach(function (c) {
      c.onclick = function () {
        active = active === c.dataset.v ? null : c.dataset.v;
        bar.querySelectorAll(".chip").forEach(function (x) { x.classList.toggle("on", x.dataset.v === active); });
        onChange(input.value.trim().toLowerCase(), active);
      };
    });
    input.oninput = function () { onChange(input.value.trim().toLowerCase(), active); };
    onChange("", null);
  }
  var STATUS_CHIPS = [["verified", "✓ verified"], ["undocumented", "＋ game only"], ["not-in-game", "✕ not in game"]];

  // ---------------------------------------------------------------- views
  function bar(c) {
    var total = c.verified + c.undocumented + c["not-in-game"] + c.unverified || 1;
    return '<div class="bar">' + [["verified", "var(--ok)"], ["undocumented", "var(--new)"], ["not-in-game", "var(--bad)"], ["unverified", "var(--unk)"]].map(function (x) {
      return '<span style="width:' + (100 * c[x[0]] / total) + "%;background:" + x[1] + '" title="' + c[x[0]] + " " + STATUS[x[0]][1] + '"></span>';
    }).join("") + "</div>";
  }
  function legend() {
    return '<div class="legend">' + keys(STATUS).map(function (s) { return pill(s) + ' <span class="muted">' + esc(STATUS[s][2]) + "</span>"; }).join("") + "</div>";
  }

  function viewHome() {
    var m = A.meta || {};
    var api = keys(A.F).filter(function (k) { return !A.F[k].ui; });
    var cf = count(api, function (k) { return A.F[k].s; });
    var ce = count(keys(A.E), function (k) { return A.E[k].s; });
    var enums = keys(A.T).filter(function (k) { return A.T[k].k === "Enumeration" || A.T[k].k === "Constants"; });
    var ct = count(enums, function (k) { return A.T[k].s; });
    var calls = A.calls || {};
    function stat(n, l, c) { return '<div class="stat"><div class="n">' + n.toLocaleString() + '</div><div class="l">' + l + "</div>" + (c ? bar(c) : "") + "</div>"; }
    var h = "<h1>WoW Forever add-on API</h1>";
    h += '<p class="lede">What this client\'s add-on API really is. Anything marked verified was confirmed by the ApiProbe add-on in game; Blizzard\'s own docs, shipped in the client, supply signatures and descriptions and stay leads until the game agrees.</p>';
    h += '<div class="stats">' + stat(api.length, "client API functions", cf) + stat(keys(A.E).length, "events", ce) + stat(enums.length, "enums and constant groups", ct) +
      stat(keys(A.W).filter(function (k) { return !A.W[k].err; }).length, "widget types") + stat(keys(A.C).length, "CVars and commands") + "</div>";
    h += legend();
    h += "<h2>Where this comes from</h2><table>";
    h += "<tr><td>Game dump</td><td>" + (m.probe ? "ApiProbe " + esc(m.probe) + " on client <code>" + esc(m.key) + "</code>, interface " + esc(m.toc) + ", " + esc(m.locale) : '<span class="pill s-unverified">none yet</span>') + "</td></tr>";
    h += "<tr><td>Getter calls</td><td>out of combat: " + (calls.outside && calls.outside.done ? "done" : "not run") + " · in combat: " + (calls.combat && calls.combat.done ? "done" : "not run") + "</td></tr>";
    h += "<tr><td>Client docs</td><td>Blizzard_APIDocumentationGenerated from client <code>" + esc(A.client) + "</code></td></tr>";
    h += "<tr><td>Events checked with</td><td>" + esc(A.eventCheck || "nothing yet") + "</td></tr>";
    h += "<tr><td>Generated</td><td>" + esc(A.generated) + "</td></tr></table>";
    h += '<h2>Good starting points</h2><ul><li><a href="#/restrictions">What changes in combat, what is secret, what is blocked</a></li>' +
      '<li><a href="#/globals">Global functions Blizzard never documented</a></li><li><a href="#/events">Events, with what was seen firing</a></li></ul>';
    if (keys(A.tainted).length) h += '<p class="note">Globals made by other add-ons were left out: ' + keys(A.tainted).sort(sortStr).map(function (k) { return esc(k) + " (" + A.tainted[k] + ")"; }).join(", ") + ".</p>";
    main.innerHTML = h;
  }

  function viewSystems() {
    main.innerHTML = '<h1>Systems</h1><p class="lede">Blizzard groups the API into systems, mostly one per <code>C_</code> namespace. Namespaces Blizzard\'s docs don\'t mention get their own entry.</p>' +
      filterBar("sf") + '<div id="sl"></div>';
    wireFilter("sf", function (q) {
      var names = pageNames.filter(function (n) { return !q || n.toLowerCase().indexOf(q) >= 0 || (pages[n].ns || "").toLowerCase().indexOf(q) >= 0; });
      bigList("sl", names, function (n) {
        var p = pages[n], c = count(p.fns, function (k) { return A.F[k].s; });
        return '<tr><td><a href="#/system/' + enc(n) + '">' + esc(n) + '</a></td><td class="mono">' + esc(p.ns || "") + "</td><td>" + p.fns.length + "</td><td>" + p.events.length +
          '</td><td style="min-width:140px">' + (p.fns.length ? '<div class="stat" style="padding:0;border:0;background:none">' + bar(c) + "</div>" : "") + "</td></tr>";
      }, "<tr><th>System</th><th>Namespace</th><th>Functions</th><th>Events</th><th>Status</th></tr>", 500);
    });
  }

  function viewSystem(name) {
    var p = pages[name];
    if (!p) return notFound(name);
    var h = "<h1>" + esc(name) + "</h1>" + (p.ns ? '<p class="lede">Namespace <code>' + esc(p.ns) + "</code></p>" : "");
    var fns = p.fns.slice().sort(sortStr);
    if (fns.length) {
      h += '<h2>Functions <span class="muted">(' + fns.length + ')</span></h2><div class="tablewrap"><table><tr><th></th><th>Function</th><th>Out of combat</th><th>In combat</th></tr>';
      fns.forEach(function (k) { var f = A.F[k]; h += "<tr><td>" + pill(f.s) + '</td><td class="mono"><a href="#/system/' + enc(name) + "/" + enc(k) + '">' + esc(k) + "</a></td><td>" + callCell(f.o) + "</td><td>" + callCell(f.c) + "</td></tr>"; });
      h += "</table></div>" + fns.map(fnCard).join("");
    }
    if (p.events.length) h += "<h2>Events</h2>" + p.events.sort(sortStr).map(eventCard).join("");
    if (p.types.length) h += "<h2>Types</h2>" + p.types.sort(sortStr).map(typeCard).join("");
    main.innerHTML = h;
  }

  function viewEvents() {
    main.innerHTML = '<h1>Events</h1><p class="lede">Checked with ' + esc(A.eventCheck || "nothing yet") + '. "Seen" counts events that fired while the probe\'s live counter was on.</p>' +
      filterBar("ef", STATUS_CHIPS.concat([["seen", "seen firing"], ["protected", "protected"]])) + '<div id="el"></div>';
    var all = keys(A.E).sort(sortStr);
    wireFilter("ef", function (q, s) {
      var items = all.filter(function (k) {
        var e = A.E[k];
        if (q && k.toLowerCase().indexOf(q) < 0) return false;
        if (s === "seen") return !!e.live;
        if (s === "protected") return e.chk === "forbidden" || e.chk === "blocked";
        return !s || e.s === s;
      });
      bigList("el", items, function (k) {
        var e = A.E[k];
        return "<tr><td>" + pill(e.s) + '</td><td class="mono"><a href="#/event/' + enc(k) + '">' + esc(k) + "</a>" + (e.chk === "forbidden" ? ' <span class="pill p-bad">protected</span>' : "") +
          "</td><td>" + (e.live ? e.live.n : "") + "</td><td>" + (e.sys ? '<a href="#/system/' + enc(e.sys) + '">' + esc(e.sys) + "</a>" : '<span class="muted">' + esc(e.u || "") + "</span>") + "</td></tr>";
      }, "<tr><th></th><th>Event</th><th>Seen</th><th>System</th></tr>");
    });
  }

  function viewTypes() {
    main.innerHTML = '<h1>Enums and structures</h1><p class="lede">Enums and constants are checked against <code>Enum</code> and <code>Constants</code> in game. Structures are table shapes from Blizzard\'s docs.</p>' +
      filterBar("tf", [["Enumeration", "enums"], ["Constants", "constants"], ["Structure", "structures"], ["undocumented", "＋ game only"], ["mismatch", "values differ"]]) + '<div id="tl"></div>';
    var all = keys(A.T).sort(sortStr);
    wireFilter("tf", function (q, s) {
      var items = all.filter(function (k) {
        var t = A.T[k];
        if (q && k.toLowerCase().indexOf(q) < 0) return false;
        if (s === "undocumented") return t.s === "undocumented";
        if (s === "mismatch") return !!t.mm;
        return !s || t.k === s;
      });
      bigList("tl", items, function (k) {
        var t = A.T[k];
        return "<tr><td>" + (t.s ? pill(t.s) : "") + '</td><td class="mono"><a href="#/type/' + enc(k) + '">' + esc(k) + "</a>" + (t.mm ? ' <span class="pill p-warn">values differ</span>' : "") +
          "</td><td>" + esc(t.k) + "</td><td>" + (t.sys ? '<a href="#/system/' + enc(t.sys) + '">' + esc(t.sys) + "</a>" : "") + "</td></tr>";
      }, "<tr><th></th><th>Name</th><th>Kind</th><th>System</th></tr>");
    });
  }

  function viewWidgets() {
    var h = '<h1>Widgets</h1><p class="lede">One object of each type was created in game and its metatable read. Methods with a Blizzard doc show its signature.</p><div class="tablewrap"><table><tr><th>Type</th><th>Methods</th><th>Script handlers</th></tr>';
    keys(A.W).sort(sortStr).forEach(function (k) {
      var w = A.W[k];
      h += w.err ? '<tr><td class="mono">' + esc(k) + '</td><td colspan="2"><span class="pill p-bad">not creatable</span> <span class="err">' + esc(w.err) + "</span></td></tr>"
        : '<tr><td class="mono"><a href="#/widget/' + enc(k) + '">' + esc(k) + "</a></td><td>" + keys(w.m).length + "</td><td>" + (w.sc || []).length + "</td></tr>";
    });
    main.innerHTML = h + "</table></div>";
  }

  function viewWidget(k) {
    var w = A.W[k];
    if (!w) return notFound(k);
    var ms = keys(w.m).sort(sortStr);
    var h = "<h1>" + esc(k) + '</h1><p class="lede">Object type reported: <code>' + esc(w.ot) + "</code> · " + ms.length + " methods</p>";
    h += "<h2>Script handlers</h2><p>" + ((w.sc || []).map(function (s) { return "<code>" + esc(s) + "</code>"; }).join(" ") || '<span class="muted">none found</span>') + "</p>";
    h += "<h2>Methods</h2>" + filterBar("wf", [["doc", "documented"], ["nodoc", "no Blizzard doc"]]) + '<div id="wl"></div>';
    main.innerHTML = h;
    wireFilter("wf", function (q, s) {
      var items = ms.filter(function (m) { return (!q || m.toLowerCase().indexOf(q) >= 0) && (!s || (s === "doc") === !!w.m[m]); });
      bigList("wl", items, function (m) {
        var sys = w.m[m], d = sys && A.O[sys] && A.O[sys][m];
        return '<tr><td class="mono">' + (d ? '<div class="sig" style="margin:0">' + esc(m) + "(" + params(d.a) + ")" + (d.r && d.r.length ? " → " + params(d.r) : "") + "</div>" : esc(m)) +
          (d && d.d ? "<p>" + esc(d.d) + "</p>" : "") + "</td><td>" + (d ? '<div class="flags">' + flagPills(d.fl) + '</div><span class="note">' + esc(sys) + "</span>" : '<span class="pill s-undocumented">＋ no doc</span>') + "</td></tr>";
      }, "<tr><th>Method</th><th>Notes</th></tr>", 400);
    });
  }

  function viewGlobals(ui) {
    var items = keys(A.F).filter(function (k) { var f = A.F[k]; return !f.sys && !f.ns && f.s === "undocumented" && !!f.ui === ui; }).sort(sortStr);
    main.innerHTML = ui
      ? '<h1>Blizzard UI functions</h1><p class="lede">Global functions written in Lua by Blizzard\'s own UI code. They exist in game, but they are UI helpers that can change with any patch, not client API.</p>' + filterBar("gf") + '<div id="gl"></div>'
      : '<h1>Undocumented globals</h1><p class="lede">In the game, in no Blizzard doc file, and not written in Blizzard\'s Lua UI: Forever additions or legacy client API. Signatures come only from what the probe saw; a no-argument call often answers with a <code>Usage:</code> error that names the arguments.</p>' +
        filterBar("gf", [["ok", "answered"], ["usage", "usage error"], ["secret", "secret in combat"]]) + '<div id="gl"></div>';
    wireFilter("gf", function (q, s) {
      var list = items.filter(function (k) {
        var f = A.F[k];
        if (q && k.toLowerCase().indexOf(q) < 0) return false;
        if (s === "ok") return f.o && f.o.n != null;
        if (s === "usage") return f.o && /Usage/.test(f.o.error || "");
        if (s === "secret") return f.c && (f.c.returns || []).some(function (v) { return /^secret/.test(v); });
        return true;
      });
      bigList("gl", list, ui ? function (k) { return '<tr><td class="mono">' + esc(k) + '</td><td class="mono muted">' + esc(typeof A.F[k].ui === "string" ? A.F[k].ui : "") + "</td></tr>"; }
        : function (k) { var f = A.F[k]; return '<tr><td class="mono"><a href="#/fn/' + enc(k) + '">' + esc(k) + "</a></td><td>" + callCell(f.o, true) + "</td><td>" + callCell(f.c) + "</td></tr>"; },
        ui ? "<tr><th>Function</th><th>Defined in</th></tr>" : "<tr><th>Function</th><th>Out of combat</th><th>In combat</th></tr>", 400);
    });
  }

  function viewRestrictions() {
    var c = A.calls || {};
    function phase(p) {
      var r = c[p] || {};
      var on = keys(r.restrictions).filter(function (k) { return r.restrictions[k] === true; });
      return (r.done ? "done" : keys(r).length ? "partial" : "not run") + (r.restrictions ? " · restrictions active: " + (on.join(", ") || "none") : "");
    }
    var fk = keys(A.F).sort(sortStr);
    var diff = fk.filter(function (k) { var f = A.F[k]; return f.o && f.c && !f.o.skipped && !f.c.skipped && JSON.stringify([f.o.n, f.o.returns, !!f.o.error]) !== JSON.stringify([f.c.n, f.c.returns, !!f.c.error]); });
    var always = fk.filter(function (k) { var r = (A.F[k].o || {}).returns; return r && r.length && r.every(function (v) { return /^secret/.test(v); }); });
    var forbidden = fk.filter(function (k) { var f = A.F[k]; return (f.o && (f.o.forbidden || /forbidden|blocked/.test(f.o.skipped || ""))) || (f.c && (f.c.forbidden || /forbidden|blocked/.test(f.c.skipped || ""))); });
    var crash = fk.filter(function (k) { var f = A.F[k]; return /crash/.test(((f.o || {}).skipped || "") + ((f.c || {}).skipped || "")); });
    var pev = keys(A.E).filter(function (k) { return A.E[k].chk === "forbidden" || A.E[k].chk === "blocked"; }).sort(sortStr);
    var h = '<h1>Restrictions seen in game</h1><p class="lede">What the probe saw, not what the docs claim. Out of combat: ' + esc(phase("outside")) + ". In combat: " + esc(phase("combat")) + ".</p>";
    function list(title, items, note) {
      return "<h2>" + title + ' <span class="muted">(' + items.length + ")</span></h2>" + (note ? '<p class="muted">' + note + "</p>" : "") +
        (items.length ? '<div class="cols">' + items.map(function (k) { return '<div><a href="#/fn/' + enc(k) + '">' + esc(k) + "</a></div>"; }).join("") + "</div>" : '<p class="muted">None.</p>');
    }
    h += "<h2>Answered differently in combat <span class=\"muted\">(" + diff.length + ')</span></h2><div class="tablewrap"><table><tr><th>Function</th><th>Out of combat</th><th>In combat</th></tr>' +
      diff.map(function (k) { return '<tr><td class="mono"><a href="#/fn/' + enc(k) + '">' + esc(k) + "</a></td><td>" + callCell(A.F[k].o, true) + "</td><td>" + callCell(A.F[k].c, true) + "</td></tr>"; }).join("") + "</table></div>";
    h += list("Secret even out of combat", always, "Every return value was secret on the first, out-of-combat run.");
    h += "<h2>Events add-ons may not register <span class=\"muted\">(" + pev.length + ')</span></h2><div class="cols">' + pev.map(function (k) { return '<div><a href="#/event/' + enc(k) + '">' + esc(k) + "</a></div>"; }).join("") + "</div>";
    h += list("Protected or blocked when called", forbidden, "Calling them raised ADDON_ACTION_FORBIDDEN or ADDON_ACTION_BLOCKED; the probe won't call them again.");
    h += list("Crashed the client", crash, "Never called again (sources/crashers.json).");
    var counts = {};
    fk.forEach(function (k) { var fl = A.F[k].fl || {}; keys(fl).forEach(function (f) { if (fl[f] !== false && /^(Secret|Requires|HasRestrictions|IsProtectedFunction)/.test(f)) counts[f] = (counts[f] || 0) + 1; }); });
    h += '<h2>Flags in Blizzard\'s docs</h2><p class="muted">How many functions carry each flag. Leads only.</p><div class="tablewrap"><table><tr><th>Flag</th><th>Functions</th></tr>' +
      keys(counts).sort(function (a, b) { return counts[b] - counts[a]; }).map(function (f) { return '<tr><td class="mono">' + esc(f) + "</td><td>" + counts[f] + "</td></tr>"; }).join("") + "</table></div>";
    main.innerHTML = h;
  }

  function viewCVars(focus) {
    main.innerHTML = '<h1>CVars and console commands</h1><p class="lede">From <code>C_Console.GetAllCommands</code> in game. Defaults only; the probe never reads current values.</p>' + filterBar("cf") + '<div id="cl"></div>';
    var all = keys(A.C).sort(sortStr);
    wireFilter("cf", function (q) {
      var items = all.filter(function (k) { var c = A.C[k]; return !q || k.toLowerCase().indexOf(q) >= 0 || String(c.h || "").toLowerCase().indexOf(q) >= 0; });
      bigList("cl", items, function (k) { var c = A.C[k]; return '<tr id="' + esc(k) + '"><td class="mono">' + esc(k) + '</td><td class="mono">' + esc(c.d == null ? "" : c.d) + "</td><td>" + esc(c.h || "") + "</td></tr>"; },
        "<tr><th>Name</th><th>Default</th><th>Help</th></tr>", 400);
    });
    if (focus) { var input = document.querySelector("#cf input"); input.value = focus; input.oninput(); }
  }

  function viewLua() {
    var h = '<h1>Lua environment</h1><p class="lede">Lua version: <code>' + esc((A.meta || {}).lua) + "</code>. <code>tostring</code> on a built-in function: <code>" + esc((A.meta || {}).fnPrint) +
      "</code>; on a Lua function: <code>" + esc((A.meta || {}).fnPrintLua) + "</code>.</p>";
    h += "<h2>Lower-case global functions</h2><div class=\"cols\">" + A.lua.map(function (k) { return "<div>" + esc(k) + "</div>"; }).join("") + "</div>";
    keys(A.libs).sort().forEach(function (lib) { h += "<h2>" + esc(lib) + '</h2><div class="cols">' + A.libs[lib].map(function (k) { return "<div>" + esc(lib + "." + k) + "</div>"; }).join("") + "</div>"; });
    main.innerHTML = h;
  }

  function single(card, back) { main.innerHTML = (back || "") + card; }
  function notFound(what) { main.innerHTML = "<h1>Not found</h1><p class=\"muted\">" + esc(what) + "</p>"; }

  // ---------------------------------------------------------------- routing
  function route() {
    var parts = location.hash.replace(/^#\/?/, "").split("/").map(decodeURIComponent);
    var view = parts[0] || "", arg = parts[1], sub = parts[2];
    document.querySelectorAll(".side > a").forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#/" + view || (view === "" && a.getAttribute("href") === "#/")); });
    document.querySelectorAll(".syslist a").forEach(function (a) { a.classList.toggle("on", view === "system" && a.dataset.n === arg); });
    document.getElementById("side").classList.remove("open");
    window.scrollTo(0, 0);
    if (view === "") viewHome();
    else if (view === "systems") viewSystems();
    else if (view === "system") { viewSystem(arg); if (sub) { var el = document.getElementById(sub); if (el) el.scrollIntoView(); } }
    else if (view === "fn") A.F[arg] ? single(fnCard(arg), A.F[arg].page ? '<p><a href="#/system/' + enc(A.F[arg].page) + '">← ' + esc(A.F[arg].page) + "</a></p>" : "") : notFound(arg);
    else if (view === "event") A.E[arg] ? single(eventCard(arg), '<p><a href="#/events">← Events</a></p>') : notFound(arg);
    else if (view === "type") A.T[arg] ? single(typeCard(arg), '<p><a href="#/types">← Enums and structures</a></p>') : notFound(arg);
    else if (view === "events") viewEvents();
    else if (view === "types") viewTypes();
    else if (view === "widgets") viewWidgets();
    else if (view === "widget") viewWidget(arg);
    else if (view === "globals") viewGlobals(false);
    else if (view === "ui") viewGlobals(true);
    else if (view === "restrictions") viewRestrictions();
    else if (view === "cvars") viewCVars(arg);
    else if (view === "lua") viewLua();
    else notFound(location.hash);
  }

  // sidebar system list
  var syslist = document.getElementById("syslist");
  function drawSys(q) {
    syslist.innerHTML = pageNames.filter(function (n) { return !q || n.toLowerCase().indexOf(q) >= 0; }).map(function (n) {
      return '<a href="#/system/' + enc(n) + '" data-n="' + esc(n) + '"><span>' + esc(n) + "</span><small>" + pages[n].fns.length + "</small></a>";
    }).join("");
  }
  drawSys("");
  document.getElementById("sysfilter").oninput = function () { drawSys(this.value.trim().toLowerCase()); };

  // global search
  var q = document.getElementById("q"), results = document.getElementById("results"), sel = -1;
  function search() {
    var s = q.value.trim().toLowerCase();
    if (s.length < 2) { results.hidden = true; return; }
    var hits = [];
    for (var i = 0; i < SEARCH.length; i++) {
      var e = SEARCH[i], at = e[0].indexOf(s);
      if (at < 0) continue;
      var last = e[0].lastIndexOf(".") + 1;
      var score = (e[0] === s ? 0 : e[0].slice(last) === s ? 1 : at === last ? 2 : at === 0 ? 3 : 5) + e[4] * 2 + (e[3] === "not-in-game" ? 1 : 0) + e[0].length / 200;
      hits.push([score, e]);
    }
    hits.sort(function (a, b) { return a[0] - b[0]; });
    sel = -1;
    results.innerHTML = hits.slice(0, 60).map(function (h) {
      var e = h[1];
      return '<a href="' + link(e[1], e[2]) + '"><span class="kind">' + esc(e[1]) + '</span><span class="name">' + esc(e[2]) + "</span>" + (e[3] ? pill(e[3]) : "") + "</a>";
    }).join("") || '<a><span class="muted">No matches</span></a>';
    results.hidden = false;
  }
  q.oninput = search;
  q.onkeydown = function (ev) {
    var items = results.querySelectorAll("a[href]");
    if (ev.key === "ArrowDown" || ev.key === "ArrowUp") {
      ev.preventDefault();
      sel = Math.max(0, Math.min(items.length - 1, sel + (ev.key === "ArrowDown" ? 1 : -1)));
      items.forEach(function (a, i) { a.classList.toggle("on", i === sel); });
      if (items[sel]) items[sel].scrollIntoView({ block: "nearest" });
    } else if (ev.key === "Enter" && items.length) {
      location.hash = items[Math.max(sel, 0)].getAttribute("href");
      results.hidden = true; q.blur();
    } else if (ev.key === "Escape") { results.hidden = true; q.blur(); }
  };
  results.onclick = function () { results.hidden = true; };
  document.addEventListener("click", function (ev) { if (!ev.target.closest(".search")) results.hidden = true; });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "/" && document.activeElement.tagName !== "INPUT") { ev.preventDefault(); q.focus(); q.select(); }
  });

  // theme and menu
  var root = document.documentElement;
  try { var saved = localStorage.getItem("forever-api-theme"); if (saved) root.dataset.theme = saved; } catch (e) { /* storage blocked */ }
  document.getElementById("theme").onclick = function () {
    var dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("forever-api-theme", root.dataset.theme); } catch (e) { /* storage blocked */ }
  };
  document.getElementById("menu").onclick = function () { document.getElementById("side").classList.toggle("open"); };

  window.addEventListener("hashchange", route);
  route();
})();
