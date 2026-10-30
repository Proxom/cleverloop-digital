/* Anonymous demand counter: page views, Buy clicks and downloads per product. No cookies, no storage, no personal data. */
(function () {
  var API = "/api/t.php";
  function send(p, e) {
    var body = JSON.stringify({ p: p, e: e });
    try {
      if (navigator.sendBeacon && navigator.sendBeacon(API, body)) return;
    } catch (x) {}
    try { fetch(API, { method: "POST", body: body, keepalive: true }); } catch (x) {}
  }
  var css = "dialog.cl-dlg{border:0;border-radius:20px;padding:0;max-width:440px;width:calc(100% - 32px);box-shadow:0 30px 80px -20px rgba(0,0,0,.5);color:#0f1b2d;font:inherit}" +
    "dialog.cl-dlg::backdrop{background:rgba(6,12,24,.55);backdrop-filter:blur(3px)}" +
    ".cl-dlg .in{padding:28px 28px 24px}.cl-dlg h2{margin:0 0 8px;font-size:1.4rem;letter-spacing:-.02em}" +
    ".cl-dlg p{margin:0 0 14px;color:#586273}.cl-dlg .row2{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}" +
    ".cl-dlg .ok{display:grid;place-items:center;width:46px;height:46px;border-radius:14px;background:#e3f6ee;color:#0f8a5f;font-size:1.5rem;margin-bottom:14px}" +
    ".cl-dlg button{font:inherit;font-weight:700;cursor:pointer}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var seen = {};
  document.querySelectorAll("[data-demand-view]").forEach(function (n) {
    var p = n.getAttribute("data-demand-view");
    if (!seen[p]) { seen[p] = 1; send(p, "view"); }
  });
  document.querySelectorAll("[data-demand-download]").forEach(function (a) {
    a.addEventListener("click", function () { send(a.getAttribute("data-demand-download"), "download"); });
  });
  document.querySelectorAll("[data-demand-click]").forEach(function (b) {
    b.addEventListener("click", function (ev) {
      ev.preventDefault();
      send(b.getAttribute("data-demand-click"), "click");
      var root = b.getAttribute("data-root") || "";
      var d = document.createElement("dialog"); d.className = "cl-dlg";
      d.innerHTML = '<div class="in"><div class="ok" aria-hidden="true">&#10003;</div><h2>Thanks, you are early!</h2>' +
        "<p>Checkout for this product is not open yet. We are measuring interest first, and your click counts toward opening it.</p>" +
        "<p>Until then, everything below is free and needs no sign-up.</p>" +
        '<div class="row2"><a class="btn btn-acc" href="' + root + 'templates/contractor-estimate-template.html">Free estimate template</a>' +
        '<a class="btn btn-ghost" href="' + root + 'tools/job-price-calculator.html" style="color:#0f1b2d">Free calculators</a></div>' +
        '<p style="margin:16px 0 0;text-align:right"><button type="button" class="x" style="background:none;border:0;color:#586273">Close</button></p></div>';
      document.body.appendChild(d);
      d.querySelector(".x").onclick = function () { d.close(); d.remove(); };
      d.addEventListener("cancel", function () { d.remove(); });
      if (d.showModal) d.showModal(); else d.setAttribute("open", "");
    });
  });
})();
