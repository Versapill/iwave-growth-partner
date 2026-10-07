// Shared behaviour for every page: footer year, header background on scroll, mobile menu
// Year
document.querySelector('[data-year]').textContent = new Date().getFullYear();

// Header background once scrolled
const header = document.querySelector('[data-header]');
const onScroll = () => {
  const scrolled = window.scrollY > 12;
  header.classList.toggle('bg-white/85', scrolled);
  header.classList.toggle('backdrop-blur-md', scrolled);
  header.classList.toggle('shadow-[0_1px_0_#E6E6EF]', scrolled);
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const menuBtn = document.querySelector('[data-menu-btn]');
const menu = document.querySelector('[data-menu]');
const setMenu = (open) => {
  menu.classList.toggle('hidden', !open);
  menuBtn.setAttribute('aria-expanded', String(open));
  menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
};
menuBtn.addEventListener('click', () => setMenu(menuBtn.getAttribute('aria-expanded') !== 'true'));
menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
