/* Estimate & Invoice Maker. Runs fully in the browser; the draft is kept only on this device (localStorage). */
(function () {
  var KEY = "cl-maker-draft-v1";
  var PRESETS = {
    "general-contractor": { label: "General contractor", items: [["Demolition and haul-away", 1, "job", 900], ["Framing labor", 24, "hr", 70], ["Lumber and materials", 1, "lot", 2400], ["Building permit", 1, "ea", 350]] },
    "plumbing": { label: "Plumbing", items: [["Labor", 3, "hr", 95], ["40-gal water heater", 1, "ea", 650], ["Fittings and supplies", 1, "lot", 85], ["Remove and dispose of old unit", 1, "ea", 75]] },
    "electrical": { label: "Electrical", items: [["Labor", 4, "hr", 90], ["20A circuit materials", 1, "lot", 140], ["GFCI outlets", 4, "ea", 28], ["Permit", 1, "ea", 75]] },
    "painting": { label: "Painting", items: [["Interior walls, 2 coats", 450, "sq ft", 2.25], ["Ceilings", 180, "sq ft", 1.75], ["Trim and baseboards", 120, "lin ft", 1.5], ["Paint and supplies", 1, "lot", 260]] },
    "roofing": { label: "Roofing", items: [["Tear-off, 1 layer", 22, "sq", 95], ["Architectural shingles, installed", 22, "sq", 260], ["Underlayment and flashing", 1, "lot", 640], ["Dumpster", 1, "ea", 450]] },
    "landscaping": { label: "Landscaping", items: [["Lawn mowing", 4, "visit", 45], ["Mulch, installed", 6, "cu yd", 85], ["Shrub trimming", 3, "hr", 55], ["Yard waste removal", 1, "load", 75]] },
    "cleaning": { label: "Cleaning", items: [["Deep clean, 3 bed / 2 bath", 1, "job", 280], ["Inside oven", 1, "ea", 35], ["Inside fridge", 1, "ea", 35], ["Interior windows", 12, "ea", 6]] },
    "handyman": { label: "Handyman", items: [["Labor", 4, "hr", 75], ["Materials", 1, "lot", 120], ["Trip charge", 1, "ea", 35]] },
    "hvac": { label: "HVAC", items: [["AC tune-up", 1, "ea", 129], ["Replace run capacitor", 1, "ea", 185], ["Refrigerant R-410A", 2, "lb", 95]] },
    "flooring": { label: "Flooring", items: [["LVP installation", 400, "sq ft", 2.5], ["LVP flooring material", 420, "sq ft", 3.2], ["Underlayment", 400, "sq ft", 0.45], ["Remove old flooring", 400, "sq ft", 1]] },
    "drywall": { label: "Drywall", items: [["Drywall patch", 3, "ea", 145], ["Hang and finish drywall", 240, "sq ft", 2.75], ["Texture match", 1, "job", 125]] },
    "pressure-washing": { label: "Pressure washing", items: [["House wash", 2400, "sq ft", 0.2], ["Driveway", 800, "sq ft", 0.18], ["Deck", 300, "sq ft", 0.35]] },
    "carpentry": { label: "Carpentry", items: [["Finish carpentry labor", 16, "hr", 65], ["Baseboard, installed", 180, "lin ft", 4.5], ["Interior door, pre-hung, installed", 3, "ea", 285], ["Trim lumber and fasteners", 1, "lot", 210]] },
    "concrete": { label: "Concrete", items: [["Excavation and grading", 1, "job", 650], ["Gravel base, 4 in", 600, "sq ft", 1.1], ["Concrete slab, 4 in, broom finish", 600, "sq ft", 7.5], ["Rebar and forms", 1, "lot", 480]] },
    "fencing": { label: "Fencing", items: [["Remove old fence", 150, "lin ft", 3], ["6 ft wood privacy fence, installed", 150, "lin ft", 32], ["Walk gate", 1, "ea", 350], ["Post holes in concrete", 19, "ea", 25]] },
    "tile": { label: "Tile", items: [["Remove old tile", 60, "sq ft", 3], ["Cement board and waterproofing", 60, "sq ft", 4], ["Tile installation", 60, "sq ft", 12], ["Grout, thinset and trim", 1, "lot", 180]] },
    "junk-removal": { label: "Junk removal", items: [["Junk removal, half truck load", 1, "load", 325], ["Mattress disposal fee", 1, "ea", 40], ["Appliance haul-away", 2, "ea", 60], ["Stairs / long carry", 1, "ea", 50]] },
    "window-cleaning": { label: "Window cleaning", items: [["Exterior windows", 24, "ea", 8], ["Interior windows", 24, "ea", 6], ["Screen cleaning", 24, "ea", 3], ["Track and sill cleaning", 24, "ea", 2]] }
  };
  window.CL_PRESETS = PRESETS;
  var today = new Date(), plus = function (d) { var x = new Date(today); x.setDate(x.getDate() + d); return x.toISOString().slice(0, 10); };
  function fresh(trade) {
    var p = PRESETS[trade] || PRESETS["handyman"];
    return {
      type: "estimate", trade: trade || "handyman", number: "1001", date: plus(0), due: plus(30),
      biz: "Your Business Name", bizInfo: "123 Main St, Springfield\n(555) 010-0000 · you@yourbusiness.com\nLicense # 000000", logo: "",
      client: "Customer Name", clientInfo: "Job address\nPhone / email",
      items: p.items.map(function (r) { return { d: r[0], q: r[1], u: r[2], r: r[3] }; }),
      tax: 0, deposit: 30, paid: 0,
      notes: "Example prices. Replace them with your own.\nPrice valid until the date above. Work not listed is extra and needs a signed change order."
    };
  }
  var S;
  var hash = (location.hash || "").slice(1);
  try { S = JSON.parse(localStorage.getItem(KEY) || "null"); } catch (e) { S = null; }
  var want = PRESETS[hash] ? hash : document.body.getAttribute("data-trade");
  if (!S) S = fresh(want || "handyman");
  else if (want && S.trade !== want) { S.trade = want; S.items = PRESETS[want].items.map(function (r) { return { d: r[0], q: r[1], u: r[2], r: r[3] }; }); }
  if (document.body.getAttribute("data-type") && !hash) S.type = document.body.getAttribute("data-type");

  var $ = function (id) { return document.getElementById(id); };
  var money = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" });
  var num = function (v) { var n = parseFloat(v); return isFinite(n) ? n : 0; };
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function totals() {
    var sub = S.items.reduce(function (a, it) { return a + num(it.q) * num(it.r); }, 0);
    var tax = sub * num(S.tax) / 100, total = sub + tax;
    var dep = S.type === "estimate" ? total * num(S.deposit) / 100 : 0;
    var paid = S.type === "invoice" ? num(S.paid) : 0;
    return { sub: sub, tax: tax, total: total, dep: dep, paid: paid, bal: total - paid };
  }

  function bindFields() {
    ["number", "date", "due", "biz", "bizInfo", "client", "clientInfo", "tax", "deposit", "paid", "notes"].forEach(function (k) {
      var el = $("f-" + k); if (!el) return;
      el.value = S[k];
      el.addEventListener("input", function () { S[k] = el.value; save(); renderPrev(); });
    });
  }
  function renderItems() {
    var host = $("items"); host.innerHTML = "";
    S.items.forEach(function (it, i) {
      var row = document.createElement("div"); row.className = "item";
      row.innerHTML = '<input aria-label="Description" value="' + esc(it.d) + '"><input aria-label="Quantity" inputmode="decimal" value="' + esc(it.q) + '"><input aria-label="Unit" value="' + esc(it.u) + '"><input aria-label="Rate in dollars" inputmode="decimal" value="' + esc(it.r) + '"><button type="button" class="del" aria-label="Remove line">&times;</button>';
      var ins = row.querySelectorAll("input"), keys = ["d", "q", "u", "r"];
      ins.forEach(function (inp, j) { inp.addEventListener("input", function () { it[keys[j]] = inp.value; save(); renderPrev(); }); });
      row.querySelector(".del").onclick = function () { S.items.splice(i, 1); save(); renderItems(); renderPrev(); };
      host.appendChild(row);
    });
  }
  function renderType() {
    document.querySelectorAll("[data-settype]").forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-settype") === S.type)); });
    $("lbl-due").textContent = S.type === "estimate" ? "Valid until" : "Due date";
    $("wrap-deposit").hidden = S.type !== "estimate";
    $("wrap-paid").hidden = S.type !== "invoice";
  }
  function renderPrev() {
    var t = totals(), isE = S.type === "estimate";
    var rows = S.items.map(function (it) {
      return "<tr><td>" + esc(it.d) + "</td><td class=r>" + esc(it.q) + " " + esc(it.u) + "</td><td class=r>" + money.format(num(it.r)) + "</td><td class=r>" + money.format(num(it.q) * num(it.r)) + "</td></tr>";
    }).join("");
    var logo = S.logo ? '<img src="' + S.logo + '" alt="">' : "";
    $("paper").innerHTML =
      '<div class="dh"><div class="biz">' + logo + "<div><b>" + esc(S.biz) + "</b><span>" + esc(S.bizInfo) + '</span></div></div>' +
      '<div class="dt"><h3>' + (isE ? "ESTIMATE" : "INVOICE") + "</h3><div>No. " + esc(S.number) + "</div><div>Date: " + esc(S.date) + "</div><div>" + (isE ? "Valid until: " : "Due: ") + esc(S.due) + "</div></div></div>" +
      '<div class="parties"><div><div class="lab">' + (isE ? "Prepared for" : "Bill to") + '</div><div class="who"><b>' + esc(S.client) + "</b>\n" + esc(S.clientInfo) + "</div></div></div>" +
      "<table><thead><tr><th>Description</th><th class=r>Qty</th><th class=r>Rate</th><th class=r>Amount</th></tr></thead><tbody>" + rows + "</tbody></table>" +
      '<div class="tots"><div><span>Subtotal</span><span>' + money.format(t.sub) + "</span></div>" +
      (num(S.tax) ? "<div><span>Sales tax (" + esc(S.tax) + "%)</span><span>" + money.format(t.tax) + "</span></div>" : "") +
      '<div class="grand"><span>Total</span><span>' + money.format(t.total) + "</span></div>" +
      (isE && num(S.deposit) ? '<div class="due"><span>Deposit to start (' + esc(S.deposit) + "%)</span><span>" + money.format(t.dep) + "</span></div>" : "") +
      (!isE && t.paid ? "<div><span>Paid</span><span>&minus;" + money.format(t.paid) + "</span></div>" : "") +
      (!isE ? '<div class="due"><span>Balance due</span><span>' + money.format(t.bal) + "</span></div>" : "") + "</div>" +
      (S.notes ? '<div class="notes"><div class="lab">Notes &amp; terms</div>' + esc(S.notes) + "</div>" : "") +
      (isE ? '<div class="sign"><div>Accepted by (customer signature)</div><div>Date</div></div>' : "") +
      '<div class="brand">Made with the free Estimate &amp; Invoice Maker at cleverloopdigital.com</div>';
  }
  function track(e) {
    try { var b = JSON.stringify({ p: "maker", e: e }); if (!(navigator.sendBeacon && navigator.sendBeacon("/api/t.php", b))) fetch("/api/t.php", { method: "POST", body: b, keepalive: true }); } catch (x) {}
  }

  bindFields(); renderItems(); renderType(); renderPrev(); track("view");
  document.querySelectorAll("[data-settype]").forEach(function (b) { b.onclick = function () { S.type = b.getAttribute("data-settype"); save(); renderType(); renderPrev(); }; });
  $("add").onclick = function () { S.items.push({ d: "", q: 1, u: "ea", r: 0 }); save(); renderItems(); renderPrev(); var l = $("items").lastElementChild; if (l) l.querySelector("input").focus(); };
  $("pdf").onclick = function () { track("download"); window.print(); };
  $("reset").onclick = function () { var tr = S.trade; S = fresh(tr); save(); bindFields(); renderItems(); renderType(); renderPrev(); };
  $("logo").addEventListener("change", function () {
    var f = this.files && this.files[0]; if (!f) return;
    if (f.size > 600000) { $("logo-msg").textContent = "Please use an image under 600 KB."; return; }
    var r = new FileReader(); r.onload = function () { S.logo = r.result; $("logo-prev").src = r.result; $("logo-prev").hidden = false; $("logo-msg").textContent = ""; save(); renderPrev(); }; r.readAsDataURL(f);
  });
  if (S.logo) { $("logo-prev").src = S.logo; $("logo-prev").hidden = false; }
  var pr = $("presets");
  Object.keys(PRESETS).forEach(function (k) {
    var b = document.createElement("button"); b.type = "button"; b.textContent = PRESETS[k].label;
    b.onclick = function () { S.trade = k; S.items = PRESETS[k].items.map(function (r) { return { d: r[0], q: r[1], u: r[2], r: r[3] }; }); save(); renderItems(); renderPrev(); };
    pr.appendChild(b);
  });
})();
