/* ═══════════════════════════════════════════════
   MS LASH & BROW — SCRIPT.JS
   Smooth Scroll · Navbar · Carousel · Catalog Filter
   ═══════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── SMOOTH SCROLL ──────────────────────────── */
  function initSmoothScroll() {
    document.querySelectorAll('.smooth-scroll').forEach(function (link) {
      link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (!href || !href.startsWith('#')) return;
        const target = document.querySelector(href);
        if (!target) return;
        e.preventDefault();
        const navbarH = document.querySelector('.navbar').offsetHeight;
        const top = target.getBoundingClientRect().top + window.scrollY - navbarH;
        window.scrollTo({ top: top, behavior: 'smooth' });
        // close mobile nav if open
        closeMobileNav();
      });
    });
  }

  /* ── NAVBAR ─────────────────────────────────── */
  function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const toggle = document.querySelector('.navbar__toggle');
    const mobileNav = document.querySelector('.navbar__mobile-nav');

    // Scroll class
    window.addEventListener('scroll', function () {
      navbar.classList.toggle('scrolled', window.scrollY > 20);
    }, { passive: true });

    // Hamburger toggle
    if (toggle && mobileNav) {
      toggle.addEventListener('click', function () {
        const isOpen = toggle.classList.toggle('open');
        mobileNav.classList.toggle('open', isOpen);
        toggle.setAttribute('aria-expanded', String(isOpen));
        mobileNav.setAttribute('aria-hidden', String(!isOpen));
      });
    }
  }

  function closeMobileNav() {
    const toggle = document.querySelector('.navbar__toggle');
    const mobileNav = document.querySelector('.navbar__mobile-nav');
    if (!toggle || !mobileNav) return;
    toggle.classList.remove('open');
    mobileNav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    mobileNav.setAttribute('aria-hidden', 'true');
  }

  /* ── CATALOG FILTER ─────────────────────────── */
  function initCatalogFilter() {
    const buttons = document.querySelectorAll('.catalog__filter-btn');
    const cards = document.querySelectorAll('.catalog__card');

    if (!buttons.length || !cards.length) return;

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        // Update active button
        buttons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');

        cards.forEach(function (card, i) {
          const cat = card.getAttribute('data-category');
          const show = filter === 'all' || cat === filter;

          if (show) {
            card.classList.remove('hidden');
            // stagger re-entry animation
            card.classList.remove('visible');
            void card.offsetWidth; // reflow
            setTimeout(function () {
              card.classList.add('visible');
            }, i * 60);
          } else {
            card.classList.add('hidden');
            card.classList.remove('visible');
          }
        });
      });
    });

    // Trigger initial animation on page load
    cards.forEach(function (card, i) {
      setTimeout(function () {
        card.classList.add('visible');
      }, 100 + i * 80);
    });
  }

  /* ── CAROUSEL PAUSE ON FOCUS ────────────────── */
  function initCarousel() {
    const outer = document.querySelector('.carousel__outer');
    const track = document.querySelector('.carousel__track');
    if (!track || !outer) return;

    // Pause when any card is focused (keyboard accessibility)
    track.querySelectorAll('.carousel__card').forEach(function (card) {
      card.addEventListener('focusin', function () {
        track.style.animationPlayState = 'paused';
      });
      card.addEventListener('focusout', function () {
        track.style.animationPlayState = '';
      });
    });

    // Touch swipe to pause
    let touchStartX = 0;
    outer.addEventListener('touchstart', function (e) {
      touchStartX = e.touches[0].clientX;
      track.style.animationPlayState = 'paused';
    }, { passive: true });

    outer.addEventListener('touchend', function () {
      track.style.animationPlayState = '';
    }, { passive: true });
  }

  /* ── SCROLL-REVEAL (Intersection Observer) ── */
  function initScrollReveal() {
    if (!('IntersectionObserver' in window)) return;

    const targets = document.querySelectorAll(
      '.section-header, .portfolio__item, .footer__brand, .footer__contact'
    );

    const css = `
      .reveal-ready { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease, transform 0.6s ease; }
      .reveal-ready.revealed { opacity: 1; transform: none; }
    `;
    const style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);

    const io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    targets.forEach(function (el, i) {
      el.classList.add('reveal-ready');
      el.style.transitionDelay = (i % 3) * 0.1 + 's';
      io.observe(el);
    });
  }

  /* ── INIT ───────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', function () {
    initNavbar();
    initSmoothScroll();
    initCatalogFilter();
    initCarousel();
    initScrollReveal();
  });

})();
