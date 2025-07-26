// Archivo JS para scripts personalizados

// Funcionalidad del menú hamburguesa
// Se encarga de abrir/cerrar el menú en móviles y tablets

document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.getElementById('hamburger-btn');
  const menu = document.getElementById('main-menu');
  const blurBg = document.getElementById('menu-blur-bg');
  const body = document.body;

  if (hamburger && menu) {
    function toggleMenu() {
      hamburger.classList.toggle('active');
      menu.classList.toggle('open');
      body.classList.toggle('menu-open');
      if (blurBg) blurBg.classList.toggle('open');
    }

    hamburger.addEventListener('click', toggleMenu);

    // Cierra el menú al hacer clic en el fondo borroso
    if (blurBg) blurBg.addEventListener('click', toggleMenu);

    // Cierra el menú al seleccionar un enlace de navegación
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (menu.classList.contains('open')) toggleMenu();
      });
    });
  }

 // Carrusel auto deslizante para contenedores con clase .carousel en móvil
  const initCarousel = scroller => {
    if (scroller.dataset.carouselInit) return; // evitar duplicar listeners
    scroller.dataset.carouselInit = 'true';
    scroller.scrollLeft = 0;
    let rafId;
    const speed = 0.5; // píxeles por frame
    const step = () => {
      scroller.scrollLeft += speed;
      if (scroller.scrollLeft >= scroller.scrollWidth - scroller.clientWidth) {
        scroller.scrollLeft = 0;
      }
      rafId = requestAnimationFrame(step);
    };

    const start = () => { if (!rafId) rafId = requestAnimationFrame(step); };
    const stop = () => { if (rafId) { cancelAnimationFrame(rafId); rafId = null; } };

    scroller.addEventListener('pointerdown', stop, { passive: true });
    scroller.addEventListener('pointerup', start);
    scroller.addEventListener('mouseenter', stop);
    scroller.addEventListener('mouseleave', start);
    start();
  };

  const mq = window.matchMedia('(max-width: 800px)');
  const enableCarousels = () => {
    document.querySelectorAll('.carousel').forEach(initCarousel);
  };

  if (mq.matches) enableCarousels();
  mq.addEventListener('change', e => {
    if (e.matches) enableCarousels();
  });
});
