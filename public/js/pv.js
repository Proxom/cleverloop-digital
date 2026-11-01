/* Cookie-free, anonymous page-view count. Sends only the page path and the referring site's domain. No cookies, no storage, no identifiers. */
(function () {
  try {
    var ref = "";
    if (document.referrer) {
      var h = new URL(document.referrer).hostname.replace(/^www\./, "");
      if (h && h !== location.hostname.replace(/^www\./, "")) ref = h;
    }
    var body = JSON.stringify({ p: location.pathname, r: ref, b: navigator.webdriver ? 1 : 0 });
    if (navigator.sendBeacon && navigator.sendBeacon("/api/pv.php", body)) return;
    fetch("/api/pv.php", { method: "POST", body: body, keepalive: true });
  } catch (e) {}
})();
