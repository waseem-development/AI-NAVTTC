// Shared interactivity for the Image Data Analysis course.
// Scroll progress, active TOC highlighting, code copy buttons, mobile nav.

(function () {
  "use strict";

  // ---- Scroll progress bar ----
  const bar = document.getElementById("progress-bar");
  function updateProgress() {
    if (!bar) return;
    const h = document.documentElement;
    const scrollTop = h.scrollTop || document.body.scrollTop;
    const height = h.scrollHeight - h.clientHeight;
    const pct = height > 0 ? (scrollTop / height) * 100 : 0;
    bar.style.width = pct.toFixed(1) + "%";
  }
  document.addEventListener("scroll", updateProgress, { passive: true });
  window.addEventListener("resize", updateProgress);

  // ---- Active section highlighting in sidebar ----
  const sections = Array.from(document.querySelectorAll("section.block[id]"));
  const navLinks = Array.from(document.querySelectorAll(".nav-link[href^='#']"));

  function setActive() {
    let currentId = null;
    const probe = window.innerHeight * 0.3;
    for (const sec of sections) {
      const rect = sec.getBoundingClientRect();
      if (rect.top <= probe) currentId = sec.id;
    }
    navLinks.forEach((link) => {
      const match = link.getAttribute("href") === "#" + currentId;
      link.classList.toggle("active", !!currentId && match);
    });
  }
  document.addEventListener("scroll", setActive, { passive: true });
  window.addEventListener("load", setActive);

  // ---- Copy buttons on code blocks ----
  document.querySelectorAll(".code-wrap").forEach((wrap) => {
    const pre = wrap.querySelector("pre.code-block");
    const btn = wrap.querySelector(".copy-btn");
    if (!pre || !btn) return;
    btn.addEventListener("click", () => {
      const text = pre.innerText;
      navigator.clipboard.writeText(text).then(() => {
        const original = btn.textContent;
        btn.textContent = "copied";
        btn.classList.add("copied");
        setTimeout(() => {
          btn.textContent = original;
          btn.classList.remove("copied");
        }, 1400);
      });
    });
  });

  // ---- Mobile sidebar toggle ----
  const toggle = document.getElementById("menu-toggle");
  const sidebar = document.querySelector(".sidebar");
  const scrim = document.getElementById("scrim");
  function closeMenu() {
    sidebar && sidebar.classList.remove("open");
    scrim && scrim.classList.remove("show");
  }
  if (toggle && sidebar) {
    toggle.addEventListener("click", () => {
      sidebar.classList.toggle("open");
      scrim && scrim.classList.toggle("show");
    });
  }
  scrim && scrim.addEventListener("click", closeMenu);
  navLinks.forEach((l) => l.addEventListener("click", closeMenu));

  // ---- Checklist persistence-free checked styling ----
  document.querySelectorAll(".checklist input[type='checkbox']").forEach((box) => {
    box.addEventListener("change", () => {
      const label = box.parentElement.querySelector("label");
      if (label) label.classList.toggle("checked", box.checked);
    });
  });
})();
