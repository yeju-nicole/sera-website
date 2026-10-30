(function () {
  var root = document.documentElement;
  root.classList.add("js");
  var params = new URLSearchParams(location.search);
  var TITLES = { ko: "SERA · SDX재단", en: "SERA · SDX Foundation" };

  // ---- embed mode for the SDX Foundation site: ?embed=1 hides the SDX bar and footer
  var framed = false;
  try { framed = window.self !== window.top; } catch (err) { framed = true; }
  if (params.get("embed") === "1") root.classList.add("embed");

  // ---- language
  function store(k, v) { try { localStorage.setItem(k, v); } catch (err) {} }
  function read(k) { try { return localStorage.getItem(k); } catch (err) { return null; } }
  function setLang(lang, save) {
    if (lang !== "en") lang = "ko";
    root.setAttribute("data-lang", lang);
    root.setAttribute("lang", lang);
    document.title = TITLES[lang];
    document.querySelectorAll("[data-lang-btn]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-lang-btn") === lang));
    });
    if (save) store("sera-lang", lang);
  }
  setLang(params.get("lang") || read("sera-lang") || "ko", false);
  document.querySelectorAll("[data-lang-btn]").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.getAttribute("data-lang-btn"), true); });
  });

  // ---- views: #charter and #principles are reading views; any other id lives in the home view
  var views = Array.prototype.slice.call(document.querySelectorAll(".view"));
  var navLinks = document.querySelectorAll("[data-nav]");
  function route(scroll) {
    var id = decodeURIComponent(location.hash.slice(1)) || "home";
    var target = document.getElementById(id);
    var view = target && (target.classList.contains("view") ? target : target.closest(".view"));
    if (!view) { view = views[0]; target = null; }
    views.forEach(function (v) { v.classList.toggle("active", v === view); });
    var current = view.id === "home" ? id : view.id;
    navLinks.forEach(function (a) { a.classList.toggle("on", a.getAttribute("data-nav") === current); });
    if (scroll !== false) {
      requestAnimationFrame(function () {
        if (!target || target === view || id === "home") window.scrollTo(0, 0);
        else target.scrollIntoView();
      });
    }
    closeMenu();
  }
  window.addEventListener("hashchange", function () { route(true); });

  // ---- mobile menu
  var menuBtn = document.getElementById("menu-btn");
  var nav = document.getElementById("nav");
  function closeMenu() { nav.classList.remove("open"); menuBtn.setAttribute("aria-expanded", "false"); }
  menuBtn.addEventListener("click", function () {
    var open = !nav.classList.contains("open");
    nav.classList.toggle("open", open);
    menuBtn.setAttribute("aria-expanded", String(open));
  });

  route(!!location.hash);

  // ---- tell a parent page our height so an iframe can size itself
  if (framed && window.parent && "ResizeObserver" in window) {
    var last = 0;
    new ResizeObserver(function () {
      var h = document.documentElement.scrollHeight;
      if (h !== last) { last = h; window.parent.postMessage({ type: "sera:height", height: h }, "*"); }
    }).observe(document.body);
  }
})();
