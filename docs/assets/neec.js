/* NEEC site script. Progressive enhancement only: every page is complete without it.
   Reads the page's data from <script id="neec-data">, written by build_site.py. */
(function () {
  "use strict";

  var DATA = {};
  var node = document.getElementById("neec-data");
  if (node) { try { DATA = JSON.parse(node.textContent); } catch (e) { DATA = {}; } }

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function cslug(c) { return c.toLowerCase().replace(".", "-"); }
  function halfUp(x) { return Math.floor(x + 0.5 + 1e-9); }
  var ROOT = (function () {
    var l = document.querySelector('link[rel="stylesheet"]');
    return l ? l.getAttribute("href").replace(/assets\/neec\.css$/, "") : "";
  })();
  var MARK = { "1": "s10", "0.5": "s05", "0": "s00" };
  var WORD = { "1": "1.0, pass", "0.5": "0.5, partial", "0": "0.0, structural failure" };

  /* ---------------------------------------------------------------- the score field */
  function initField() {
    var table = $("#field");
    var F = DATA.field;
    if (!table || !F) return;
    var wrap = table.closest(".field-wrap");
    var pop = $("#pop");
    var rows = $$("tbody tr[data-s]", table);
    var grid = rows.map(function (r) { return $$("td.m", r); });
    var litC = null, litRow = null, hideTimer = null, current = null;

    grid.forEach(function (row, i) {
      row.forEach(function (td, j) {
        td.tabIndex = i === 0 && j === 0 ? 0 : -1;
        td.setAttribute("data-i", i);
        td.setAttribute("data-j", j);
      });
    });

    function light(c) {
      if (litC === c) return;
      if (litC) $$('[data-c="' + litC + '"]', table).forEach(function (n) { n.classList.remove("lit"); });
      litC = c;
      if (c) $$('[data-c="' + c + '"]', table).forEach(function (n) { n.classList.add("lit"); });
    }
    function lightRow(tr) {
      if (litRow === tr) return;
      if (litRow) litRow.classList.remove("lit-row");
      litRow = tr;
      if (tr) tr.classList.add("lit-row");
    }
    function place(td) {
      var r = td.getBoundingClientRect(), w = wrap.getBoundingClientRect();
      var left = r.left - w.left + r.width / 2 - pop.offsetWidth / 2;
      left = Math.max(0, Math.min(left, w.width - pop.offsetWidth));
      var top = r.bottom - w.top + 8;
      if (r.bottom + pop.offsetHeight + 24 > window.innerHeight && r.top - pop.offsetHeight - 16 > 0) {
        top = r.top - w.top - pop.offsetHeight - 8;
      }
      pop.style.left = left + "px";
      pop.style.top = top + "px";
    }
    function show(td) {
      clearTimeout(hideTimer);
      current = td;
      var c = td.getAttribute("data-c"), tr = td.parentNode, s = tr.getAttribute("data-s");
      var cr = F.criteria[c], sy = F.systems[s];
      var cls = ["s10", "s05", "s00", "sp", "sn"].filter(function (k) { return td.classList.contains(k); })[0];
      var label = $(".vh", td).textContent;
      light(c);
      lightRow(tr);
      pop.innerHTML = '<span class="pc">' + esc(c) + '</span><span class="pn">' + esc(cr[0]) + "</span>" +
        '<span class="ps"><span class="mk ' + cls + '" aria-hidden="true"></span>' + esc(sy[0]) + ": " + esc(label) + "</span>" +
        '<a href="' + ROOT + "systems/" + sy[1] + ".html#" + cslug(c) + '">' +
        (F.publish ? "Evidence and reasons" : "The system's page") + "</a> &nbsp; " +
        '<a href="' + ROOT + "criteria/" + cslug(c) + '.html">The criterion</a>';
      pop.hidden = false;
      place(td);
    }
    function hide(now) {
      clearTimeout(hideTimer);
      hideTimer = setTimeout(function () {
        pop.hidden = true;
        current = null;
        light(null);
        lightRow(null);
      }, now ? 0 : 180);
    }
    function move(td) {
      $$('td.m[tabindex="0"]', table).forEach(function (n) { n.tabIndex = -1; });
      td.tabIndex = 0;
      td.focus({ preventScroll: false });
    }

    table.addEventListener("mouseover", function (e) {
      var td = e.target.closest && e.target.closest("td.m");
      if (td) { show(td); return; }
      var th = e.target.closest && e.target.closest("th.ch");
      if (th) { light(th.getAttribute("data-c")); }
    });
    table.addEventListener("mouseleave", function () { if (!pop.matches(":hover")) hide(); });
    pop.addEventListener("mouseenter", function () { clearTimeout(hideTimer); });
    pop.addEventListener("mouseleave", function () { hide(); });
    table.addEventListener("focusin", function (e) {
      var td = e.target.closest && e.target.closest("td.m");
      if (td) show(td);
    });
    table.addEventListener("click", function (e) {
      var td = e.target.closest && e.target.closest("td.m");
      if (td) move(td);
    });
    document.addEventListener("focusin", function (e) {
      if (!wrap.contains(e.target)) hide(true);
    });
    table.addEventListener("keydown", function (e) {
      var td = e.target.closest && e.target.closest("td.m");
      if (!td) return;
      var i = +td.getAttribute("data-i"), j = +td.getAttribute("data-j"), n = null;
      if (e.key === "ArrowRight") n = grid[i][j + 1];
      else if (e.key === "ArrowLeft") n = grid[i][j - 1];
      else if (e.key === "ArrowDown") n = grid[i + 1] && grid[i + 1][j];
      else if (e.key === "ArrowUp") n = grid[i - 1] && grid[i - 1][j];
      else if (e.key === "Home") n = grid[i][0];
      else if (e.key === "End") n = grid[i][grid[i].length - 1];
      else if (e.key === "Enter") { var a = $("a", pop); if (a) a.click(); return; }
      else if (e.key === "Escape") { hide(true); return; }
      else return;
      e.preventDefault();
      if (n) move(n);
    });
    window.addEventListener("resize", function () { if (current && !pop.hidden) place(current); });

    if (document.body.classList.contains("p-home")) {
      var seen = false;
      try { seen = sessionStorage.getItem("neec-settled") === "1"; sessionStorage.setItem("neec-settled", "1"); } catch (e) { seen = false; }
      if (!seen) table.classList.add("settle");
    }
  }

  /* ---------------------------------------------------------------- copy and download */
  function selectText(el) {
    var r = document.createRange();
    r.selectNodeContents(el);
    var s = window.getSelection();
    s.removeAllRanges();
    s.addRange(r);
    try { return document.execCommand("copy"); } catch (e) { return false; }
  }
  function initCopy() {
    $$("[data-copy]").forEach(function (b) {
      b.addEventListener("click", function () {
        var t = $(b.getAttribute("data-copy"));
        if (!t) return;
        var st = b.parentNode.querySelector(".copy-status");
        function done(ok) {
          if (!st) return;
          st.textContent = ok ? "Copied." : "Selected. Press Ctrl+C (or Cmd+C) to copy.";
          setTimeout(function () { st.textContent = ""; }, 4000);
        }
        if (navigator.clipboard && window.isSecureContext) {
          navigator.clipboard.writeText(t.textContent).then(function () { done(true); }, function () { done(selectText(t)); });
        } else {
          done(selectText(t));
        }
      });
    });
  }

  /* ---------------------------------------------------------------- the AI prompt */
  function renderPrompt(P, mode, system, criterion) {
    var drop = mode === "audit" ? "blind" : "audit";
    var t = P.template.replace(new RegExp("\\[\\[" + drop + "\\]\\][\\s\\S]*?\\[\\[/" + drop + "\\]\\]\\n?", "g"), "");
    t = t.split("[[" + mode + "]]\n").join("").split("[[/" + mode + "]]\n").join("");
    var sys = P.systems[system];
    function rep(k, v) { t = t.split("{{" + k + "}}").join(v); }
    rep("MODE", mode);
    rep("MODE_LABEL", mode === "audit" ? "audit the published scores" : "score blind, without the published scores");
    rep("SYSTEM", sys ? sys.name : P.no_system);
    rep("CRITERIA", criterion ? criterion : "all " + Object.keys(P.per).length + " criteria");
    rep("CRITERIA_TEXT", criterion ? P.per[criterion] : P.all);
    rep("DOCUMENTS", sys ? sys.docs.map(function (d) { return "   - " + d; }).join("\n") : P.no_docs);
    return t;
  }
  function initPrompt() {
    var form = $("[data-prompt]"), P = DATA.prompt;
    if (!form || !P) return;
    var pre = $("#prompt-text"), dl = $("[data-download]"), url = null;
    var q = new URLSearchParams(window.location.search);
    if (q.get("system") && P.systems[q.get("system")]) form.elements.system.value = q.get("system");
    if (q.get("criterion") && P.per[q.get("criterion")]) form.elements.criterion.value = q.get("criterion");
    if (q.get("mode") === "blind") form.querySelector('input[value="blind"]').checked = true;
    function render() {
      var mode = form.querySelector('input[name="mode"]:checked').value;
      var s = form.elements.system.value, c = form.elements.criterion.value;
      var text = renderPrompt(P, mode, s, c);
      pre.textContent = text;
      if (dl && window.Blob && window.URL) {
        if (url) URL.revokeObjectURL(url);
        url = URL.createObjectURL(new Blob([text], { type: "text/markdown;charset=utf-8" }));
        dl.href = url;
        dl.setAttribute("download", "neec-ai-prompt-" + mode + (s ? "-" + s.toLowerCase() : "") + (c ? "-" + cslug(c) : "") + ".md");
      }
    }
    form.addEventListener("change", render);
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    render();
  }

  /* ---------------------------------------------------------------- the WJP bar (C4.6 clause 3) */
  function initWJP() {
    var box = $("[data-wjp]"), W = DATA.wjp;
    if (!box || !W) return;
    var svg = $("#wjp-strip", box), range = $("#wjp-bar", box), out = $("#wjp-out", box), ed = $("#wjp-ed", box), read = $("#wjp-read", box);
    var NS = "http://www.w3.org/2000/svg";
    var refRows = $$("table.refs tbody tr", box);
    var names = {};
    W.refs.forEach(function (r) { names[r[0]] = r[1]; });
    function r2(x) { return Math.round(x * 100) / 100; }
    function el(tag, attrs, text) {
      var n = document.createElementNS(NS, tag);
      for (var k in attrs) n.setAttribute(k, attrs[k]);
      if (text != null) n.textContent = text;
      svg.appendChild(n);
      return n;
    }
    function verdicts(vals, bar) { return vals.map(function (v) { return v == null ? null : v >= bar - 1e-9; }); }
    function draw() {
      var bar = parseFloat(range.value), edition = ed.value, rows = W.data[edition];
      out.textContent = bar.toFixed(2);
      var byCode = {};
      rows.forEach(function (r) { byCode[r[0]] = r2(r[2]); });
      while (svg.firstChild && svg.lastChild.nodeName !== "title") svg.removeChild(svg.lastChild);
      var width = svg.clientWidth || 720, H = 150, axisY = 118, lo = 0.1, hi = 1.0, pad = 10;
      svg.setAttribute("viewBox", "0 0 " + width + " " + H);
      function x(v) { return pad + (v - lo) / (hi - lo) * (width - 2 * pad); }
      el("rect", { x: x(bar), y: 52, width: Math.max(0, x(hi) - x(bar)), height: axisY - 52, "class": "zone" });
      el("line", { x1: x(lo), x2: x(hi), y1: axisY, y2: axisY, "class": "axis" });
      for (var t = 1; t <= 10; t++) {
        var v = t / 10;
        el("line", { x1: x(v), x2: x(v), y1: axisY, y2: axisY + 4, "class": "axis" });
        el("text", { x: x(v), y: axisY + 17, "text-anchor": "middle", "class": "tick" }, v.toFixed(1));
      }
      var stack = {};
      rows.forEach(function (r) {
        var v = r2(r[2]);
        if (names[r[0]]) return;
        var k = v.toFixed(2);
        stack[k] = (stack[k] || 0) + 1;
        var cy = axisY - 6 - (stack[k] - 1) * 6.5;
        var c = el("circle", { cx: x(v), cy: cy, r: 2.8, "class": "dot" + (v >= bar - 1e-9 ? " meets" : "") });
        var tt = document.createElementNS(NS, "title");
        tt.textContent = r[1] + ", " + v.toFixed(2);
        c.appendChild(tt);
      });
      el("line", { x1: x(bar), x2: x(bar), y1: 50, y2: axisY + 4, "class": "bar" });
      var refs = W.refs.filter(function (r) { return byCode[r[0]] != null; })
        .map(function (r) { return { code: r[0], name: r[1], v: byCode[r[0]] }; })
        .sort(function (a, b) { return a.v - b.v; });
      var lanes = [];
      refs.forEach(function (r) {
        var w = r.name.length * 6.6 + 8, cx = x(r.v), lane = 0;
        while (lanes[lane] != null && lanes[lane] > cx - w / 2) lane++;
        lanes[lane] = cx + w / 2;
        var ly = 12 + lane * 14;
        el("line", { x1: cx, x2: cx, y1: ly + 3, y2: axisY - 6, "class": "ref-line" });
        el("circle", { cx: cx, cy: axisY - 6, r: 4.2, "class": "ref" });
        el("text", { x: cx, y: ly, "text-anchor": "middle", "class": "ref-l" }, r.name);
      });
      var meets = rows.filter(function (r) { return r2(r[2]) >= bar - 1e-9; }).length;
      var vals = W.refs.map(function (r) { return byCode[r[0]]; });
      var now = verdicts(vals, bar), adopted = verdicts(vals, W.bar);
      var lowB = null, highB = null;
      for (var b = 1; b < 100; b++) {
        var vv = verdicts(vals, b / 100);
        if (vv.every(function (x, i) { return x === now[i]; })) { if (lowB == null) lowB = b / 100; highB = b / 100; }
      }
      refRows.forEach(function (tr, i) {
        var code = tr.getAttribute("data-code"), v = byCode[code];
        var cells = tr.querySelectorAll("td");
        cells[1].textContent = v == null ? "not in this edition" : v.toFixed(2);
        cells[2].textContent = v == null ? "" : (v >= bar - 1e-9 ? "meets" : "does not meet");
        tr.classList.toggle("meets", v != null && v >= bar - 1e-9);
        tr.classList.toggle("changed", v != null && now[i] !== adopted[i]);
      });
      var changed = W.refs.filter(function (r, i) { return vals[i] != null && now[i] !== adopted[i]; }).map(function (r) { return r[1]; });
      var msg = "At " + bar.toFixed(2) + ", " + meets + " of " + rows.length + " jurisdictions in the " + edition +
        " edition meet the bar. Every bar from " + lowB.toFixed(2) + " to " + highB.toFixed(2) +
        " gives the reference economies the same verdicts as this one.";
      if (changed.length) msg += " Compared with the adopted bar of " + W.bar.toFixed(2) + ", the verdict changes for " + changed.join(" and ") + ".";
      read.textContent = msg;
    }
    range.addEventListener("input", draw);
    ed.addEventListener("change", draw);
    $$("[data-snap]", box).forEach(function (b) {
      b.addEventListener("click", function () { range.value = b.getAttribute("data-snap"); draw(); });
    });
    window.addEventListener("resize", draw);
    draw();
  }

  /* ---------------------------------------------------------------- weights */
  function domOfMap(S) {
    var m = {};
    S.domains.forEach(function (d) { d[2].forEach(function (c) { m[c] = d[0]; }); });
    return m;
  }
  function competition(values) {
    return values.map(function (v) { return 1 + values.filter(function (w) { return w > v + 1e-9; }).length; });
  }
  function initWeights() {
    var box = $("[data-weights]"), S = DATA.scores;
    if (!box || !S) return;
    var list = $(".rank-list", box), dws = $(".dws", box), dom = domOfMap(S);
    function weights(choice) {
      var w = {};
      S.scored.forEach(function (c) { w[c] = 1; });
      if (choice === "custom") {
        $$("input[data-dom]", box).forEach(function (i) {
          var k = parseFloat(i.value);
          S.scored.forEach(function (c) { if (dom[c] === i.getAttribute("data-dom")) w[c] = k; });
        });
      } else {
        var sc = S.schemes[+choice];
        S.scored.forEach(function (c) { w[c] = (sc.domains[dom[c]] || 1) * (sc.criteria[c] || 1); });
      }
      return w;
    }
    function pctOf(s, w) {
      var t = 0, m = 0;
      S.scored.forEach(function (c) { t += s.vector[c] * w[c]; m += w[c]; });
      return m > 0 ? (t / m) * 100 : 0;
    }
    function render() {
      var choice = box.querySelector('input[name="scheme"]:checked').value;
      dws.disabled = choice !== "custom";
      $$("output[data-for]", box).forEach(function (o) {
        o.textContent = parseFloat(box.querySelector('input[data-dom="' + o.getAttribute("data-for") + '"]').value).toFixed(1);
      });
      var w = weights(choice), eq = weights("0");
      var p = S.systems.map(function (s) { return pctOf(s, w); }), e = S.systems.map(function (s) { return pctOf(s, eq); });
      var rk = competition(p), rke = competition(e);
      var rows = S.systems.map(function (s, i) {
        var tied = rk.filter(function (r) { return r === rk[i]; }).length > 1;
        return { s: s, p: p[i], e: e[i], rank: rk[i], tied: tied, move: rke[i] - rk[i] };
      }).sort(function (a, b) { return b.p - a.p || a.s.short.localeCompare(b.s.short); });
      list.innerHTML = rows.map(function (r) {
        var mv = r.move === 0 ? "=" : (r.move > 0 ? "\u2191" + r.move : "\u2193" + (-r.move));
        var mvt = r.move === 0 ? "same place as with equal weights" : (r.move > 0 ? "up " + r.move : "down " + (-r.move)) + " from equal weights";
        return '<li><span class="rk">' + r.rank + (r.tied ? "=" : "") + '</span><span class="nm"><a href="' + ROOT + "systems/" + r.s.slug + '.html">' +
          esc(r.s.short) + '</a></span><span class="bar-bg" title="' + halfUp(r.p) + "% (equal weights " + halfUp(r.e) + '%)"><span class="bar-fg" style="width:' +
          r.p.toFixed(2) + '%"></span><span class="bar-eq" style="left:' + r.e.toFixed(2) + '%"></span></span><span class="mv ' +
          (r.move > 0 ? "up" : r.move < 0 ? "down" : "") + '"><span aria-hidden="true">' + mv + '</span><span class="vh">' + halfUp(r.p) + "%, " + mvt + "</span></span></li>";
      }).join("");
    }
    box.addEventListener("input", render);
    box.addEventListener("change", render);
    render();
  }

  /* ---------------------------------------------------------------- close calls */
  function initCalls() {
    var box = $("[data-calls]"), S = DATA.scores;
    if (!box || !S) return;
    var out = $(".calls-out", box);
    function render() {
      var id = box.querySelector('input[name="reading"]:checked').value;
      var rows = S.systems.map(function (s) {
        var r = null;
        s.readings.forEach(function (x) { if (x.id === id) r = x.result; });
        if (!r) r = { total: s.total, failures: s.failures, tier: s.tier };
        return { s: s, r: r, changed: r.tier !== s.tier };
      }).sort(function (a, b) { return b.r.total - a.r.total || a.s.short.localeCompare(b.s.short); });
      var moved = rows.filter(function (x) { return x.changed; });
      var lead = id === "scored" ? "The scores as published." :
        (moved.length ? moved.length + " system" + (moved.length > 1 ? "s change" : " changes") + " tier: " +
          moved.map(function (x) { return esc(x.s.short) + " (" + esc(x.s.tier) + " to " + esc(x.r.tier) + ")"; }).join("; ") + "."
          : "No system changes tier.");
      out.innerHTML = "<p>" + lead + '</p><div class="table-scroll"><table class="list"><thead><tr><th scope="col">System</th>' +
        '<th scope="col" class="num">Total</th><th scope="col" class="num">Failures</th><th scope="col">Tier</th></tr></thead><tbody>' +
        rows.map(function (x) {
          return '<tr' + (x.changed ? ' class="changed"' : "") + '><th scope="row"><a href="' + ROOT + "systems/" + x.s.slug + '.html#close-calls">' +
            esc(x.s.short) + '</a></th><td class="num">' + x.r.total.toFixed(1) + '</td><td class="num">' + x.r.failures +
            "</td><td>" + esc(x.r.tier) + "</td></tr>";
        }).join("") + "</tbody></table></div>";
    }
    box.addEventListener("change", render);
    render();
  }

  /* ---------------------------------------------------------------- compare */
  function initCompare() {
    var form = $("[data-compare]"), S = DATA.scores;
    if (!form || !S) return;
    var out = $(".cmp-out");
    var by = {};
    S.systems.forEach(function (s) { by[s.code] = s; });
    function dominates(a, b) {
      var ge = true, gt = 0;
      S.scored.forEach(function (c) { if (a.vector[c] < b.vector[c]) ge = false; if (a.vector[c] > b.vector[c]) gt++; });
      return ge && gt > 0 ? gt : 0;
    }
    function render() {
      var codes = [];
      $$("select", form).forEach(function (s) { if (s.value && codes.indexOf(s.value) < 0) codes.push(s.value); });
      var sys = codes.map(function (c) { return by[c]; });
      if (!sys.length) { out.innerHTML = ""; return; }
      var html = sys.map(function (s) {
        var marks = S.domains.map(function (d) {
          return d[2].map(function (c) {
            var v = s.vector[c];
            return v == null ? '<span class="mk sp" title="' + c + ' not scored"></span>' :
              '<span class="mk ' + MARK[String(v)] + '" title="' + c + ": " + WORD[String(v)] + '"></span>';
          }).join("");
        }).join('<span class="gap"></span>');
        return '<div class="cmp-row"><span class="cmp-name"><a href="' + ROOT + "systems/" + s.slug + '.html">' + esc(s.short) +
          '</a></span><span class="cmp-marks" aria-hidden="true">' + marks + '</span><span class="cmp-tot">' + s.total.toFixed(1) +
          ", " + s.failures + " failures, " + esc(s.tier) + "</span></div>";
      }).join("");
      var notes = [];
      for (var i = 0; i < sys.length; i++) {
        for (var j = i + 1; j < sys.length; j++) {
          var a = sys[i], b = sys[j], ab = dominates(a, b), ba = dominates(b, a);
          if (ab) notes.push(esc(a.short) + " scores at least as high as " + esc(b.short) + " on every criterion, and higher on " + ab + ".");
          else if (ba) notes.push(esc(b.short) + " scores at least as high as " + esc(a.short) + " on every criterion, and higher on " + ba + ".");
          else {
            var ah = 0, bh = 0;
            S.scored.forEach(function (c) { if (a.vector[c] > b.vector[c]) ah++; if (b.vector[c] > a.vector[c]) bh++; });
            notes.push("Neither of " + esc(a.short) + " and " + esc(b.short) + " dominates: the first is higher on " + ah +
              " criteria, the second on " + bh + ".");
          }
        }
      }
      out.innerHTML = html + (notes.length ? '<ul class="cmp-notes">' + notes.map(function (n) { return "<li>" + n + "</li>"; }).join("") + "</ul>" : "");
    }
    form.addEventListener("change", render);
  }

  /* ---------------------------------------------------------------- the visual suite */
  var SVGNS = "http://www.w3.org/2000/svg";
  function svgEl(parent, tag, attrs, text) {
    var n = document.createElementNS(SVGNS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    parent.appendChild(n);
    return n;
  }
  function clearSvg(svg) {
    $$(":scope > :not(title)", svg).forEach(function (n) { svg.removeChild(n); });
  }
  function scoredIn(S, crits) { return crits.filter(function (c) { return S.scored.indexOf(c) >= 0; }); }
  function domainShares(S, s) {
    return S.domains.map(function (d) {
      var cs = scoredIn(S, d[2]), t = 0;
      cs.forEach(function (c) { t += s.vector[c]; });
      return cs.length ? t / cs.length : 0;
    });
  }
  function median(a) {
    var b = a.slice().sort(function (x, y) { return x - y; }), m = b.length >> 1;
    return b.length % 2 ? b[m] : (b[m - 1] + b[m]) / 2;
  }
  var SHAPES = ["circle", "square", "diamond"];
  function marker(g, shape, x, y, cls) {
    if (shape === "circle") return svgEl(g, "circle", { cx: x, cy: y, r: 3.6, "class": cls });
    if (shape === "square") return svgEl(g, "rect", { x: x - 3.4, y: y - 3.4, width: 6.8, height: 6.8, "class": cls });
    return svgEl(g, "path", { d: "M" + x + "," + (y - 4.6) + "l4.6,4.6l-4.6,4.6l-4.6,-4.6z", "class": cls });
  }
  function drawRadar(svg, axes, series, ref) {
    clearSvg(svg);
    var W = 460, H = 400, cx = 230, cy = 205, R = 132, n = axes.length;
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    function pt(i, r) {
      var a = -Math.PI / 2 + i * 2 * Math.PI / n;
      return [cx + Math.cos(a) * R * r, cy + Math.sin(a) * R * r];
    }
    function poly(vals) { return vals.map(function (v, i) { return pt(i, v).map(function (x) { return x.toFixed(1); }).join(","); }).join(" "); }
    [0.25, 0.5, 0.75, 1].forEach(function (r) {
      svgEl(svg, "polygon", { points: poly(axes.map(function () { return r; })), "class": "ring" });
    });
    axes.forEach(function (name, i) {
      var e = pt(i, 1), l = pt(i, 1.17);
      svgEl(svg, "line", { x1: cx, y1: cy, x2: e[0], y2: e[1], "class": "spoke" });
      var cos = Math.cos(-Math.PI / 2 + i * 2 * Math.PI / n);
      var t = svgEl(svg, "text", { x: l[0], y: l[1], "text-anchor": Math.abs(cos) < 0.2 ? "middle" : (cos > 0 ? "start" : "end"), "class": "ax-l" });
      var words = name.split(" "), lines = words.length > 1 && name.length > 13 ? [words.slice(0, Math.ceil(words.length / 2)).join(" "), words.slice(Math.ceil(words.length / 2)).join(" ")] : [name];
      lines.forEach(function (ln, k) { svgEl(t, "tspan", { x: l[0], dy: k === 0 ? (lines.length > 1 ? "-0.2em" : "0.35em") : "1.15em" }, ln); });
    });
    [0.5, 1].forEach(function (r) {
      var p = pt(0, r);
      svgEl(svg, "text", { x: p[0] + 5, y: p[1] + 11, "class": "ring-l" }, (r * 100) + "%");
    });
    if (ref) svgEl(svg, "polygon", { points: poly(ref), "class": "ref" });
    series.forEach(function (s, k) {
      var g = svgEl(svg, "g", { "class": "rs rs" + k });
      svgEl(g, "polygon", { points: poly(s.values) });
      s.values.forEach(function (v, i) {
        var q = pt(i, v), m = marker(g, SHAPES[k], q[0], q[1], "mkr");
        var tt = document.createElementNS(SVGNS, "title");
        tt.textContent = s.label + ", " + axes[i] + ": " + halfUp(v * 100) + "%";
        m.appendChild(tt);
      });
    });
  }
  function legendHtml(series) {
    return series.map(function (s, k) {
      return '<span class="rl rl' + k + '"><svg viewBox="0 0 26 10" aria-hidden="true"><line x1="0" y1="5" x2="26" y2="5"/></svg>' + esc(s.label) + "</span>";
    }).join("") + '<span class="rl rlref"><svg viewBox="0 0 26 10" aria-hidden="true"><line x1="0" y1="5" x2="26" y2="5"/></svg>Median of all systems</span>';
  }
  function initProfile() {
    var P = DATA.profile, svg = $('svg[data-radar="profile"]');
    if (!P || !svg) return;
    drawRadar(svg, P.axes, [{ label: P.name, values: P.values }], P.median);
  }
  function initProfiles() {
    var form = $("[data-profiles]"), S = DATA.scores, svg = $("#radar-findings");
    if (!form || !S || !svg) return;
    var by = {};
    S.systems.forEach(function (s) { by[s.code] = s; });
    var axes = S.domains.map(function (d) { return d[1]; });
    var all = S.systems.map(function (s) { return domainShares(S, s); });
    var ref = axes.map(function (_, i) { return median(all.map(function (v) { return v[i]; })); });
    var leg = $(".radar-legend");
    function render() {
      var seen = [], series = [];
      $$("select", form).forEach(function (sel) {
        var c = sel.value;
        if (c && seen.indexOf(c) < 0) { seen.push(c); series.push({ label: by[c].short, values: domainShares(S, by[c]) }); }
      });
      drawRadar(svg, axes, series, ref);
      leg.innerHTML = legendHtml(series);
    }
    form.addEventListener("change", render);
    render();
  }
  function initTotals() {
    var table = $("[data-totals]");
    if (!table) return;
    var body = $("tbody", table), btns = $$("[data-order]");
    function order(kind) {
      var rows = $$("tr", body);
      rows.sort(function (a, b) {
        var ta = +a.getAttribute("data-total"), tb = +b.getAttribute("data-total");
        if (kind === "tier") { var d = +a.getAttribute("data-tier") - +b.getAttribute("data-tier"); if (d) return d; }
        return tb - ta || a.getAttribute("data-name").localeCompare(b.getAttribute("data-name"));
      });
      rows.forEach(function (r) { body.appendChild(r); });
      btns.forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-order") === kind)); });
    }
    btns.forEach(function (b) { b.addEventListener("click", function () { order(b.getAttribute("data-order")); }); });
  }
  function initFrontier() {
    var form = $("[data-frontier]"), S = DATA.scores, svg = $("#scatter"), read = $("#frontier-read");
    if (!form || !S || !svg) return;
    var tierIx = {};
    S.tiers.forEach(function (t, i) { tierIx[t[0]] = i; });
    var names = { total: "Total" };
    S.domains.forEach(function (d) { names[d[0]] = d[1]; });
    var wrap = svg.parentNode, tip = document.createElement("div"), pinned = null, hideT = null;
    tip.className = "pop sc-pop";
    tip.hidden = true;
    tip.setAttribute("role", "status");
    wrap.appendChild(tip);
    function place(c) {
      var r = c.getBoundingClientRect(), w = wrap.getBoundingClientRect();
      var left = r.left - w.left + r.width / 2 - tip.offsetWidth / 2;
      left = Math.max(0, Math.min(left, w.width - tip.offsetWidth));
      var top = r.top - w.top - tip.offsetHeight - 10;
      if (r.top - tip.offsetHeight - 16 < 0) top = r.bottom - w.top + 10;
      tip.style.left = left + "px";
      tip.style.top = top + "px";
    }
    function show(c, html) { clearTimeout(hideT); tip.innerHTML = html; tip.hidden = false; place(c); }
    function hide() { clearTimeout(hideT); tip.hidden = true; }
    function unpin() {
      $$(".pt.sel", svg).forEach(function (n) { n.classList.remove("sel"); n.setAttribute("aria-expanded", "false"); });
      pinned = null;
    }
    tip.addEventListener("mouseenter", function () { clearTimeout(hideT); });
    tip.addEventListener("mouseleave", function () { if (!pinned) hideT = setTimeout(hide, 160); });
    svg.addEventListener("click", function (e) { if (pinned && !(e.target.classList && e.target.classList.contains("pt"))) { unpin(); hide(); } });
    document.addEventListener("click", function (e) { if (pinned && !wrap.contains(e.target)) { unpin(); hide(); } });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !tip.hidden) { unpin(); hide(); } });
    window.addEventListener("resize", function () { var c = svg.querySelector(".pt.sel"); if (c && !tip.hidden) place(c); });
    function tipHtml(g, p, onF, kx, ky) {
      return g.map(function (q) {
        return '<span class="pn"><a href="' + ROOT + "systems/" + q.s.slug + '.html">' + esc(q.s.short) + "</a></span>" +
          '<span class="tt">' + q.s.total.toFixed(1) + " of " + S.scored.length + ", " + q.s.failures + " structural failure" +
          (q.s.failures === 1 ? "" : "s") + ", " + esc(q.s.tier) + "</span>";
      }).join("") + '<span class="tt axes">' + esc(names[kx]) + ": " + halfUp(p.x) + "%<br>" + esc(names[ky]) + ": " + halfUp(p.y) + "%</span>" +
        (onF ? '<span class="tt on-f">On the frontier of these two dimensions</span>' : "");
    }
    function value(s, key) {
      if (key === "total") return s.total / S.scored.length * 100;
      var i = S.domains.map(function (d) { return d[0]; }).indexOf(key);
      return domainShares(S, s)[i] * 100;
    }
    function render() {
      unpin();
      hide();
      clearSvg(svg);
      var kx = form.elements.fx.value, ky = form.elements.fy.value;
      var W = 760, H = 470, L = 58, B = 52, T = 18, Rr = 30;
      svg.setAttribute("viewBox", "0 0 " + W + " " + H);
      function X(v) { return L + v / 100 * (W - L - Rr); }
      function Y(v) { return H - B - v / 100 * (H - B - T); }
      [0, 25, 50, 75, 100].forEach(function (v) {
        svgEl(svg, "line", { x1: X(0), x2: X(100), y1: Y(v), y2: Y(v), "class": "sc-grid" });
        svgEl(svg, "line", { x1: X(v), x2: X(v), y1: Y(0), y2: Y(100), "class": "sc-grid" });
        svgEl(svg, "text", { x: L - 8, y: Y(v) + 4, "text-anchor": "end", "class": "sc-t" }, v + "%");
        svgEl(svg, "text", { x: X(v), y: H - B + 18, "text-anchor": "middle", "class": "sc-t" }, v + "%");
      });
      svgEl(svg, "text", { x: (L + W - Rr) / 2, y: H - 10, "text-anchor": "middle", "class": "sc-ax" },
        names[kx] + (kx === "total" ? ", share of all points" : ", share of its points"));
      svgEl(svg, "text", { x: 14, y: (T + H - B) / 2, "text-anchor": "middle", "class": "sc-ax", transform: "rotate(-90 14 " + (T + H - B) / 2 + ")" },
        names[ky] + (ky === "total" ? ", share of all points" : ", share of its points"));
      var pts = S.systems.map(function (s) { return { s: s, x: value(s, kx), y: value(s, ky) }; });
      var front = pts.filter(function (p) {
        return !pts.some(function (q) { return q.x >= p.x - 1e-9 && q.y >= p.y - 1e-9 && (q.x > p.x + 1e-9 || q.y > p.y + 1e-9); });
      }).sort(function (a, b) { return a.x - b.x || b.y - a.y; });
      if (front.length > 1) {
        var d = "M" + X(front[0].x) + "," + Y(front[0].y);
        for (var i = 1; i < front.length; i++) d += "H" + X(front[i].x) + "V" + Y(front[i].y);
        svgEl(svg, "path", { d: d, "class": "fr" });
      }
      var groups = {};
      pts.forEach(function (p) { var k = p.x.toFixed(3) + "," + p.y.toFixed(3); (groups[k] = groups[k] || []).push(p); });
      Object.keys(groups).forEach(function (k) {
        var g = groups[k], p = g[0], onF = front.indexOf(p) >= 0 || g.some(function (q) { return front.indexOf(q) >= 0; });
        var best = Math.min.apply(null, g.map(function (q) { return tierIx[q.s.tier]; }));
        var c = svgEl(svg, "circle", { cx: X(p.x), cy: Y(p.y), r: 4.5 + 1.6 * (g.length - 1), "class": "pt t" + best + (onF ? " front" : ""),
          tabindex: "0", role: "button", "aria-expanded": "false",
          "aria-label": g.map(function (q) { return q.s.short + ", " + q.s.tier; }).join("; ") + ". " + names[kx] + " " + halfUp(p.x) +
            "%, " + names[ky] + " " + halfUp(p.y) + "%" + (onF ? ". On the frontier." : ".") });
        (function (c, k, html) {
          function toggle(e) {
            e.stopPropagation();
            if (pinned === k) { unpin(); hide(); return; }
            unpin();
            pinned = k;
            c.classList.add("sel");
            c.setAttribute("aria-expanded", "true");
            show(c, html);
          }
          c.addEventListener("mouseenter", function () { if (!pinned) show(c, html); });
          c.addEventListener("mouseleave", function () { if (!pinned) hideT = setTimeout(hide, 160); });
          c.addEventListener("focus", function () { if (!pinned) show(c, html); });
          c.addEventListener("blur", function () { if (!pinned) hideT = setTimeout(hide, 160); });
          c.addEventListener("click", toggle);
          c.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(e); } });
        })(c, k, tipHtml(g, p, onF, kx, ky));
        if (onF) {
          var right = X(p.x) < W - 190;
          svgEl(svg, "text", { x: X(p.x) + (right ? 10 : -10), y: Y(p.y) - 8, "text-anchor": right ? "start" : "end", "class": "fr-l" },
            g.map(function (q) { return q.s.short; }).join(" / "));
        }
      });
      var rest = pts.length - front.length;
      read.textContent = "On " + names[kx].toLowerCase() + " and " + names[ky].toLowerCase() + ", the frontier is " +
        front.map(function (p) { return p.s.short; }).join(", ") + ": no other system scores at least as high on both and higher on one. " +
        (rest ? "Each of the other " + rest + " has at least one frontier system that scores at least as high on both and higher on one." : "");
    }
    form.addEventListener("change", render);
    render();
  }
  function initStructure() {
    var svg = $("svg.structure");
    if (!svg) return;
    function clear() { svg.classList.remove("tracing"); $$(".on", svg).forEach(function (n) { n.classList.remove("on"); }); }
    function trace(attr, val) {
      clear();
      svg.classList.add("tracing");
      $$('.lk[' + attr + '="' + val + '"]', svg).forEach(function (l) {
        l.classList.add("on");
        var n = svg.querySelector('.pn[data-n="' + l.getAttribute("data-n") + '"]'), c = svg.querySelector('.cn[data-c="' + l.getAttribute("data-c") + '"]');
        if (n) n.classList.add("on");
        if (c) c.classList.add("on");
      });
    }
    $$(".pn", svg).forEach(function (g) {
      var f = function () { trace("data-n", g.getAttribute("data-n")); };
      g.addEventListener("mouseenter", f); g.addEventListener("focus", f);
      g.addEventListener("mouseleave", clear); g.addEventListener("blur", clear);
    });
    $$(".cn", svg).forEach(function (a) {
      var f = function () { trace("data-c", a.getAttribute("data-c")); };
      a.addEventListener("mouseenter", f); a.addEventListener("focus", f);
      a.addEventListener("mouseleave", clear); a.addEventListener("blur", clear);
    });
  }

  function init() {
    initField();
    initCopy();
    initPrompt();
    initWJP();
    initWeights();
    initCalls();
    initCompare();
    initProfile();
    initProfiles();
    initTotals();
    initFrontier();
    initStructure();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
