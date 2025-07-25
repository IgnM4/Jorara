// Archivo JS para scripts personalizados

// Funcionalidad del menú hamburguesa
// Se encarga de abrir/cerrar el menú en móviles y tablets

document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.getElementById('hamburger-btn');
  const menu = document.getElementById('main-menu');
  const blurBg = document.getElementById('menu-blur-bg');
  const body = document.body;

  if (!hamburger || !menu) return;

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
});
