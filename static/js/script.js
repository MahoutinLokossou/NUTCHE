// FARINE — script.js
// Handles the mobile nav toggle and the gallery category filters.
// Language switching itself is a server-side redirect (see components/navbar.html),
// so no JS is needed for that — it works even with JS disabled.

document.addEventListener("DOMContentLoaded", () => {
  initNavToggle();
  initGalleryFilters();
});

function initNavToggle() {
  const toggle = document.querySelector("[data-nav-toggle]");
  const links = document.querySelector("[data-nav-links]");

  if (!toggle || !links) return;

  toggle.addEventListener("click", () => {
    const isOpen = links.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });

  // Close the menu when a link is tapped (mobile)
  links.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      links.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}

function initGalleryFilters() {
  const buttons = document.querySelectorAll("[data-filter]");
  const items = document.querySelectorAll("[data-category]");

  if (!buttons.length || !items.length) return;

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const filter = button.getAttribute("data-filter");

      buttons.forEach((b) => b.classList.remove("is-active"));
      button.classList.add("is-active");

      items.forEach((item) => {
        const category = item.getAttribute("data-category");
        const show = filter === "all" || filter === category;
        item.style.display = show ? "" : "none";
      });
    });
  });
}