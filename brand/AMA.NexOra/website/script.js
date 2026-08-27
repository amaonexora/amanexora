const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();

const button = document.querySelector('.menu-toggle');
const nav = document.querySelector('.site-nav');

const setNavigationOpen = open => {
  nav?.classList.toggle('open', open);
  button?.setAttribute('aria-expanded', String(open));
};

button?.addEventListener('click', () => {
  setNavigationOpen(!nav?.classList.contains('open'));
});

nav?.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => setNavigationOpen(false));
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    setNavigationOpen(false);
    button?.focus();
  }
});

window.addEventListener('resize', () => {
  if (window.innerWidth > 900) setNavigationOpen(false);
});

const revealElements = document.querySelectorAll('.reveal');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (reducedMotion || !('IntersectionObserver' in window)) {
  revealElements.forEach(element => element.classList.add('visible'));
} else {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  revealElements.forEach(element => observer.observe(element));
}
