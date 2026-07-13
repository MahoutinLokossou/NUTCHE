// Drives every .carousel on the page (products, pillars, etc.) with a
// self-looping, draggable marquee. Each carousel's track content must be
// duplicated exactly once in the DOM, so the loop point is always
// track.scrollWidth / 2.
(function () {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) return; // CSS fallback (static, wrapped) stands as-is

  document.querySelectorAll('.carousel').forEach(initCarousel);

  function initCarousel(carousel) {
    const track = carousel.querySelector('.carousel__track');
    if (!track) return;

    const SPEED = 40;          // px per second
    const TAP_THRESHOLD = 10;  // px of movement below which a touch counts as a "tap"

    let offset = 0;
    let halfWidth = track.scrollWidth / 2;
    let hoverPaused = false;   // desktop hover
    let tapPaused = false;     // toggled by a tap on touchscreens — persists until tapped again
    let dragging = false;
    let dragStartX = 0;
    let dragStartOffset = 0;
    let touchMoved = false;
    let lastTimestamp = null;

    function recalc() {
      halfWidth = track.scrollWidth / 2;
    }
    window.addEventListener('resize', recalc);
    track.querySelectorAll('img').forEach((img) => {
      if (!img.complete) img.addEventListener('load', recalc, { once: true });
    });

    function setOffset(value) {
      offset = ((value % halfWidth) + halfWidth) % halfWidth;
      track.style.transform = `translateX(${-offset}px)`;
    }

    function tick(timestamp) {
      if (lastTimestamp === null) lastTimestamp = timestamp;
      const delta = (timestamp - lastTimestamp) / 1000;
      lastTimestamp = timestamp;

      if (!hoverPaused && !tapPaused && !dragging) {
        setOffset(offset + SPEED * delta);
      }
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);

    // Desktop: pause on hover, resume on leave
    carousel.addEventListener('mouseenter', () => { hoverPaused = true; });
    carousel.addEventListener('mouseleave', () => { hoverPaused = false; });

    // Desktop: drag-to-scroll
    track.style.cursor = 'grab';
    track.addEventListener('mousedown', (e) => {
      dragging = true;
      dragStartX = e.clientX;
      dragStartOffset = offset;
      track.style.cursor = 'grabbing';
    });
    window.addEventListener('mousemove', (e) => {
      if (!dragging) return;
      setOffset(dragStartOffset - (e.clientX - dragStartX));
    });
    window.addEventListener('mouseup', () => {
      dragging = false;
      track.style.cursor = 'grab';
    });

    // Touch: a genuine tap toggles tapPaused; a drag scrolls the track instead
    track.addEventListener('touchstart', (e) => {
      dragging = true;
      touchMoved = false;
      dragStartX = e.touches[0].clientX;
      dragStartOffset = offset;
    }, { passive: true });

    track.addEventListener('touchmove', (e) => {
      if (!dragging) return;
      const delta = e.touches[0].clientX - dragStartX;
      if (Math.abs(delta) > TAP_THRESHOLD) touchMoved = true;
      setOffset(dragStartOffset - delta);
    }, { passive: true });

    track.addEventListener('touchend', () => {
      dragging = false;
      if (!touchMoved) {
        // Was a tap, not a drag — toggle the stop/resume state
        tapPaused = !tapPaused;
      }
    });
  }
})();