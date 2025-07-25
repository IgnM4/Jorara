import os

# Contenidos de los archivos principales

contenido_readme = """# AgroConsultora Cerezas
Sitio web para consultora agrícola especialista en cerezas de exportación en Chile.
Generado automáticamente con estructura profesional y diseño moderno.
"""

contenido_css = """:root {
    --cereza: #A82331;
    --verde: #417505;
    --blanco: #fff;
    --gris-claro: #f3f3f3;
    --negro: #1b1b1b;
    --amarillo: #f2c94c;
    --fuente-titulos: 'Montserrat', Arial, Helvetica, sans-serif;
    --fuente-cuerpo: 'Open Sans', Arial, Helvetica, sans-serif;
}
body {
    margin: 0;
    font-family: var(--fuente-cuerpo);
    background: var(--gris-claro);
    color: var(--negro);
}
/* --- NAV --- */
header {
    background: var(--blanco);
    box-shadow: 0 2px 8px rgba(168,35,49,0.07);
    position: sticky;
    top: 0;
    z-index: 100;
}
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1200px;
    margin: auto;
    padding: 0.8rem 2rem;
}
.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.logo img {
    width: 40px;
    height: 40px;
}
.nav-links {
    list-style: none;
    display: flex;
    gap: 2rem;
    margin: 0;
    padding: 0;
}
.nav-links a {
    text-decoration: none;
    color: var(--negro);
    font-weight: 500;
    padding: 0.5rem 0;
    transition: color 0.2s;
}
.nav-links a.active,
.nav-links a:hover {
    color: var(--cereza);
    border-bottom: 2px solid var(--cereza);
}
.btn-principal {
    background: var(--cereza);
    color: var(--blanco);
    padding: 0.6rem 1.3rem;
    border-radius: 28px;
    font-family: var(--fuente-titulos);
    font-size: 1rem;
    border: none;
    cursor: pointer;
    text-decoration: none;
    font-weight: 600;
    transition: background 0.2s, color 0.2s;
}
.btn-principal:hover { background: var(--verde); color: var(--blanco); }
/* HERO */
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--blanco);
    padding: 2.5rem 2rem 2rem 2rem;
    min-height: 400px;
    max-width: 1200px;
    margin: 1.5rem auto;
    border-radius: 24px;
    box-shadow: 0 4px 24px rgba(168,35,49,0.04);
    gap: 2rem;
}
.hero-content {
    max-width: 48%;
}
.hero-content h1 {
    font-family: var(--fuente-titulos);
    font-size: 2.5rem;
    color: var(--cereza);
    margin-bottom: 0.8rem;
}
.hero-content p {
    font-size: 1.2rem;
    color: var(--negro);
    margin-bottom: 1.5rem;
}
.btn-hero {
    background: var(--verde);
    color: var(--blanco);
    padding: 0.8rem 2rem;
    font-size: 1.1rem;
    border-radius: 32px;
    text-decoration: none;
    font-weight: 700;
    transition: background 0.2s;
}
.btn-hero:hover { background: var(--cereza); }
.hero-img img {
    width: 380px;
    height: auto;
    border-radius: 20px;
    box-shadow: 0 2px 18px rgba(65,117,5,0.08);
}
@media (max-width: 900px) {
    .hero { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
    .hero-content, .hero-img { max-width: 100%; }
    .hero-img img { width: 100%; }
}
/* ---- SERVICIOS DESTACADOS ---- */
.servicios-destacados {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 2rem;
}
.servicios-destacados h2 {
    text-align: center;
    font-family: var(--fuente-titulos);
    color: var(--verde);
    font-size: 2rem;
    margin-bottom: 1.8rem;
}
.servicios-cards {
    display: flex;
    gap: 2rem;
    justify-content: center;
    flex-wrap: wrap;
}
.card {
    background: var(--blanco);
    box-shadow: 0 4px 18px rgba(65,117,5,0.07);
    border-radius: 20px;
    padding: 2rem 1.5rem;
    flex: 1 1 240px;
    max-width: 300px;
    min-width: 220px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: transform 0.2s;
}
.card:hover { transform: translateY(-6px) scale(1.04); box-shadow: 0 10px 26px rgba(168,35,49,0.09); }
.card img { width: 56px; height: 56px; margin-bottom: 1rem; }
.card h3 { color: var(--cereza); font-family: var(--fuente-titulos); font-size: 1.12rem; margin: 0.4rem 0 0.6rem 0; }
.card p { font-size: 0.98rem; color: var(--negro); margin-bottom: 1rem; }
.btn-link {
    color: var(--verde);
    font-weight: 600;
    text-decoration: none;
    font-size: 0.98rem;
    border-bottom: 1.5px solid var(--amarillo);
    padding-bottom: 2px;
    transition: color 0.2s, border-color 0.2s;
}
.btn-link:hover { color: var(--cereza); border-color: var(--cereza); }
/* ---- DIFERENCIADORES ---- */
.porque-elegirnos {
    background: var(--verde);
    color: var(--blanco);
    padding: 2.5rem 0 2.2rem 0;
    border-radius: 22px;
    margin: 3rem 2rem 2rem 2rem;
    max-width: 1200px;
    margin-left: auto; margin-right: auto;
}
.porque-elegirnos h2 {
    text-align: center;
    font-family: var(--fuente-titulos);
    font-size: 2rem;
    margin-bottom: 2rem;
}
.diferenciadores {
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
}
.diferenciadores .item {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 140px;
}
.diferenciadores .item img {
    width: 38px;
    height: 38px;
    margin-bottom: 0.7rem;
}
.diferenciadores .item p {
    font-size: 1.07rem;
    font-weight: 600;
    color: var(--blanco);
}
/* ---- BLOG / NOTICIAS ---- */
.blog-noticias {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 2rem;
}
.blog-noticias h2 {
    font-family: var(--fuente-titulos);
    color: var(--cereza);
    font-size: 1.7rem;
    margin-bottom: 1.5rem;
    text-align: left;
}
.blog-cards {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
    justify-content: flex-start;
}
.blog-card {
    background: var(--blanco);
    box-shadow: 0 2px 12px rgba(168,35,49,0.08);
    border-radius: 16px;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    max-width: 450px;
    min-width: 280px;
    margin-bottom: 1.5rem;
}
.blog-card img {
    width: 120px;
    height: 100%;
    object-fit: cover;
}
.blog-text {
    padding: 1rem 1rem;
}
.blog-text h4 {
    font-family: var(--fuente-titulos);
    color: var(--verde);
    margin: 0 0 0.5rem 0;
    font-size: 1.05rem;
}
.blog-text p {
    font-size: 0.97rem;
    margin-bottom: 0.4rem;
    color: var(--negro);
}
/* ---- CLIENTES / PARTNERS ---- */
.clientes {
    background: var(--gris-claro);
    padding: 2rem 0;
    text-align: center;
}
.clientes h2 {
    color: var(--verde);
    font-family: var(--fuente-titulos);
    font-size: 1.2rem;
    margin-bottom: 1.2rem;
}
.logos-clientes {
    display: flex;
    gap: 2.5rem;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
}
.logos-clientes img {
    max-width: 110px;
    max-height: 54px;
    object-fit: contain;
    filter: grayscale(40%);
    opacity: 0.92;
    transition: filter 0.2s, opacity 0.2s;
}
.logos-clientes img:hover { filter: none; opacity: 1; }
/* ---- FOOTER ---- */
footer {
    background: var(--negro);
    color: var(--blanco);
    padding: 2rem 0;
    font-size: 0.99rem;
    border-top-left-radius: 18px;
    border-top-right-radius: 18px;
    margin-top: 2.5rem;
}
.footer-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    max-width: 1200px;
    margin: auto;
    gap: 2.5rem;
    flex-wrap: wrap;
}
.footer-logo {
    width: 38px;
    height: 38px;
    margin-bottom: 0.8rem;
}
footer h4 {
    font-family: var(--fuente-titulos);
    color: var(--amarillo);
    margin-bottom: 0.6rem;
}
footer a { color: var(--blanco); text-decoration: underline; }
footer a:hover { color: var(--amarillo); }
/* ---- RESPONSIVE ---- */
@media (max-width: 700px) {
    .navbar, .hero, .servicios-cards, .diferenciadores, .footer-container, .blog-cards, .logos-clientes {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 1.2rem !important;
    }
    .navbar { padding: 0.5rem 1rem; }
    .hero { padding: 1rem; }
    .servicios-cards, .diferenciadores, .blog-cards, .logos-clientes { gap: 1rem; }
    .footer-container { gap: 1rem; }
    .blog-card { max-width: 100%; min-width: 180px; }
}
::-webkit-scrollbar { width: 8px; background: var(--gris-claro); }
::-webkit-scrollbar-thumb { background: var(--cereza); border-radius: 6px; }
"""

contenido_js = "// Archivo JS para scripts personalizados\n"

# Navegación, footer y head común
head_html = """
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgroConsultora Chile — Especialistas en Cerezas</title>
    <link rel="stylesheet" href="css/estilos.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:700,400|Open+Sans:400,700&display=swap" rel="stylesheet">
"""

nav_html = """
    <header>
        <nav class="navbar">
            <div class="logo">
                <img src="assets/img/logo-cerezas.png" alt="Logo AgroConsultora" />
                <span>AgroConsultora Chile</span>
            </div>
            <ul class="nav-links">
                <li><a href="index.html">Inicio</a></li>
                <li><a href="servicios.html">Servicios</a></li>
                <li><a href="nosotros.html">Nosotros</a></li>
                <li><a href="proyectos.html">Proyectos</a></li>
                <li><a href="recursos.html">Recursos</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
            <a href="contacto.html" class="btn-principal">Solicita tu Asesoría</a>
        </nav>
    </header>
"""

footer_html = """
    <footer>
        <div class="footer-container">
            <div>
                <img src="assets/img/logo-cerezas.png" alt="Logo AgroConsultora" class="footer-logo" />
                <p>&copy; 2024 AgroConsultora Chile. Todos los derechos reservados.</p>
            </div>
            <div>
                <h4>Contacto</h4>
                <ul>
                    <li>Email: <a href="mailto:info@agroconsultora.cl">info@agroconsultora.cl</a></li>
                    <li>WhatsApp: <a href="https://wa.me/56912345678" target="_blank">+56 9 1234 5678</a></li>
                    <li>Dirección: Santiago, Chile</li>
                </ul>
            </div>
            <div>
                <h4>Redes</h4>
                <ul>
                    <li><a href="#">LinkedIn</a></li>
                    <li><a href="#">Instagram</a></li>
                </ul>
            </div>
        </div>
    </footer>
"""

# Cuerpo de cada página
contenido_index = f"""<!DOCTYPE html>
<html lang="es">
<head>
    {head_html}
</head>
<body>
    {nav_html.replace('<a href="index.html">Inicio</a>', '<a href="index.html" class="active">Inicio</a>')}
    <section class="hero">
        <div class="hero-content">
            <h1>Excelencia en Consultoría Agrícola para la Industria de la Cereza</h1>
            <p>Impulsamos la innovación, productividad y éxito exportador en el rubro cerecero de Chile.</p>
            <a href="contacto.html" class="btn-hero">Solicita tu Asesoría</a>
        </div>
        <div class="hero-img">
            <img src="assets/img/hero-cerezas.jpg" alt="Cerezos en producción">
        </div>
    </section>
    <section class="servicios-destacados">
        <h2>Servicios Especializados</h2>
        <div class="servicios-cards">
            <div class="card">
                <img src="assets/icons/consultoria.svg" alt="Consultoría">
                <h3>Consultorías a Productores y Exportadores</h3>
                <p>Soluciones personalizadas para maximizar el potencial de tu campo y tu negocio.</p>
                <a href="servicios.html#consultorias" class="btn-link">Ver más</a>
            </div>
            <div class="card">
                <img src="assets/icons/charlas.svg" alt="Charlas y Conferencias">
                <h3>Charlas y Conferencias</h3>
                <p>Capacitación técnica, tendencias, liderazgo y eventos sectoriales de alto impacto.</p>
                <a href="servicios.html#charlas" class="btn-link">Ver más</a>
            </div>
            <div class="card">
                <img src="assets/icons/investigacion.svg" alt="Investigación">
                <h3>Investigación & Desarrollo</h3>
                <p>Proyectos de I+D, transferencia tecnológica y metodologías de vanguardia.</p>
                <a href="servicios.html#investigacion" class="btn-link">Ver más</a>
            </div>
            <div class="card">
                <img src="assets/icons/mejoras.svg" alt="Mejoras Productivas">
                <h3>Mejoras Productivas</h3>
                <p>Optimización de procesos, manejo eficiente de recursos y resultados medibles.</p>
                <a href="servicios.html#mejoras" class="btn-link">Ver más</a>
            </div>
        </div>
    </section>
    <section class="porque-elegirnos">
        <h2>¿Por qué elegirnos?</h2>
        <div class="diferenciadores">
            <div class="item">
                <img src="assets/icons/experiencia.svg" alt="Experiencia">
                <p>+15 años de experiencia</p>
            </div>
            <div class="item">
                <img src="assets/icons/resultados.svg" alt="Resultados">
                <p>Resultados comprobados</p>
            </div>
            <div class="item">
                <img src="assets/icons/cobertura.svg" alt="Cobertura">
                <p>Cobertura nacional y regional</p>
            </div>
            <div class="item">
                <img src="assets/icons/innovacion.svg" alt="Innovación">
                <p>Metodología innovadora</p>
            </div>
        </div>
    </section>
    <section class="blog-noticias">
        <h2>Últimas Noticias</h2>
        <div class="blog-cards">
            <div class="blog-card">
                <img src="assets/img/blog1.jpg" alt="Charla reciente">
                <div class="blog-text">
                    <h4>Charla técnica sobre nuevas variedades de cereza</h4>
                    <p>¡Conoce los principales hallazgos y recomendaciones de nuestra última conferencia!</p>
                    <a href="recursos.html#blog1" class="btn-link">Leer más</a>
                </div>
            </div>
            <div class="blog-card">
                <img src="assets/img/blog2.jpg" alt="Innovación en riego">
                <div class="blog-text">
                    <h4>Innovaciones en manejo de riego para cerezas exportables</h4>
                    <p>Las claves para lograr calidad exportadora en cada temporada.</p>
                    <a href="recursos.html#blog2" class="btn-link">Leer más</a>
                </div>
            </div>
        </div>
    </section>
    <section class="clientes">
        <h2>Confían en nosotros</h2>
        <div class="logos-clientes">
            <img src="assets/img/cliente1.png" alt="Cliente 1">
            <img src="assets/img/cliente2.png" alt="Cliente 2">
            <img src="assets/img/cliente3.png" alt="Cliente 3">
        </div>
    </section>
    {footer_html}
</body>
</html>
"""

contenido_servicios = f"""<!DOCTYPE html>
<html lang="es">
<head>
    {head_html}
</head>
<body>
    {nav_html.replace('<a href="servicios.html">Servicios</a>', '<a href="servicios.html" class="active">Servicios</a>')}
    <section class="servicios-destacados">
        <h2>Nuestros Servicios</h2>
        <div class="servicios-cards">
            <div class="card" id="consultorias">
                <img src="assets/icons/consultoria.svg" alt="Consultoría">
                <h3>Consultorías a Productores y Exportadores</h3>
                <p>Asesoría técnica y estratégica para maximizar el rendimiento y la rentabilidad de tus campos de cerezos.</p>
            </div>
            <div class="card" id="charlas">
                <img src="assets/icons/charlas.svg" alt="Charlas y Conferencias">
                <h3>Charlas y Conferencias</h3>
                <p>Capacitación y actualización para empresas, equipos técnicos y productores en temas clave del rubro.</p>
            </div>
            <div class="card" id="investigacion">
                <img src="assets/icons/investigacion.svg" alt="Investigación y Desarrollo">
                <h3>Investigación & Desarrollo</h3>
                <p>Proyectos de innovación y transferencia tecnológica para mejorar la competitividad del sector.</p>
            </div>
            <div class="card" id="mejoras">
                <img src="assets/icons/mejoras.svg" alt="Mejoras Productivas">
                <h3>Mejoras Productivas</h3>
                <p>Optimización de procesos, reducción de costos y aumento de calidad para empresas exportadoras.</p>
            </div>
        </div>
    </section>
    <section class="porque-elegirnos">
        <h2>Preguntas Frecuentes</h2>
        <div class="diferenciadores">
            <div class="item">
                <img src="assets/icons/faq.svg" alt="FAQ">
                <p>¿Trabajan con empresas de cualquier región?</p>
            </div>
            <div class="item">
                <img src="assets/icons/faq.svg" alt="FAQ">
                <p>¿Pueden adaptar la consultoría a mi presupuesto?</p>
            </div>
            <div class="item">
                <img src="assets/icons/faq.svg" alt="FAQ">
                <p>¿Ofrecen asesoría post-proyecto?</p>
            </div>
        </div>
    </section>
    {footer_html}
</body>
</html>
"""

contenido_nosotros = f"""<!DOCTYPE html>
<html lang="es">
<head>
    {head_html}
</head>
<body>
    {nav_html.replace('<a href="nosotros.html">Nosotros</a>', '<a href="nosotros.html" class="active">Nosotros</a>')}
    <section class="servicios-destacados">
        <h2>Nuestra Historia y Misión</h2>
        <p>AgroConsultora Chile nace para potenciar la industria de la cereza, aportando conocimiento técnico, pasión y resultados a productores y exportadores.</p>
        <h2>Equipo</h2>
        <div class="servicios-cards">
            <div class="card">
                <img src="assets/img/consultor1.jpg" alt="Consultor">
                <h3>Ing. Agrónomo Jefe</h3>
                <p>Especialista en fruticultura, más de 20 años en investigación y terreno.</p>
            </div>
            <div class="card">
                <img src="assets/img/consultor2.jpg" alt="Consultor">
                <h3>Director de Proyectos</h3>
                <p>Experto en innovación y transferencia tecnológica, gestión de equipos multidisciplinarios.</p>
            </div>
        </div>
        <h2>Reconocimientos</h2>
        <div class="logos-clientes">
            <img src="assets/img/premio1.png" alt="Premio 1">
            <img src="assets/img/asociacion1.png" alt="Asociación">
        </div>
    </section>
    {footer_html}
</body>
</html>
"""

contenido_proyectos = f"""<!DOCTYPE html>
<html lang="es">
<head>
    {head_html}
</head>
<body>
    {nav_html.replace('<a href="proyectos.html">Proyectos</a>', '<a href="proyectos.html" class="active">Proyectos</a>')}
    <section class="servicios-destacados">
        <h2>Proyectos y Casos de Éxito</h2>
        <div class="servicios-cards">
            <div class="card">
                <img src="assets/img/proyecto1.jpg" alt="Proyecto 1">
                <h3>Optimización de Riego en VII Región</h3>
                <p>Resultados: +23% productividad y ahorro de agua en 2 temporadas.</p>
            </div>
            <div class="card">
                <img src="assets/img/proyecto2.jpg" alt="Proyecto 2">
                <h3>Exportación de Nuevas Variedades</h3>
                <p>Asesoría integral desde la plantación hasta la logística internacional.</p>
            </div>
            <div class="card">
                <img src="assets/img/proyecto3.jpg" alt="Proyecto 3">
                <h3>Capacitación a Equipos Técnicos</h3>
                <p>+120 técnicos capacitados en manejo postcosecha y calidad.</p>
            </div>
        </div>
        <h2>Testimonios</h2>
        <div class="diferenciadores">
            <div class="item">
                <img src="assets/icons/testimonio.svg" alt="Testimonio">
                <p>“Gracias a AgroConsultora triplicamos nuestras exportaciones en solo 2 años.”</p>
            </div>
            <div class="item">
                <img src="assets/icons/testimonio.svg" alt="Testimonio">
                <p>“El enfoque humano y técnico marca la diferencia en cada etapa del trabajo.”</p>
            </div>
        </div>
    </section>
    {footer_html}
</body>
</html>
"""

contenido_recursos = f"""<!DOCTYPE html>
<html lang="es">
<head>
    {head_html}
</head>
<body>
    {nav_html.replace('<a href="recursos.html">Recursos</a>', '<a href="recursos.html" class="active">Recursos</a>')}
    <section class="servicios-destacados">
        <h2>Blog & Noticias</h2>
        <div class="blog-cards">
            <div class="blog-card">
                <img src="assets/img/blog1.jpg" alt="Charla reciente">
                <div class="blog-text">
                    <h4>Charla técnica sobre nuevas variedades de cereza</h4>
                    <p>¡Conoce los principales hallazgos y recomendaciones de nuestra última conferencia!</p>
                    <a href="#" class="btn-link">Leer más</a>
                </div>
            </div>
            <div class="blog-card">
                <img src="assets/img/blog2.jpg" alt="Innovación en riego">
                <div class="blog-text">
                    <h4>Innovaciones en manejo de riego para cerezas exportables</h4>
                    <p>Las claves para lograr calidad exportadora en cada temporada.</p>
                    <a href="#" class="btn-link">Leer más</a>
                </div>
            </div>
        </div>
        <h2>Descargas</h2>
        <div class="servicios-cards">
            <div class="card">
                <img src="assets/icons/descarga.svg" alt="Guía PDF">
                <h3>Guía de riego eficiente</h3>
                <p><a href="#" class="btn-link">Descargar PDF</a></p>
            </div>
            <div class="card">
                <img src="assets/icons/descarga.svg" alt="Checklist">
                <h3>Checklist de exportación</h3>
                <p><a href="#" class="btn-link">Descargar PDF</a></p>
            </div>
        </div>
    </section>
    {footer_html}
</body>
</html>
"""

contenido_contacto = f"""<!DOCTYPE html>
<html lang="es">
<head>
    {head_html}
</head>
<body>
    {nav_html.replace('<a href="contacto.html">Contacto</a>', '<a href="contacto.html" class="active">Contacto</a>')}
    <section class="servicios-destacados">
        <h2>Contáctanos</h2>
        <form action="mailto:info@agroconsultora.cl" method="POST" enctype="text/plain" style="max-width:450px;margin:auto;">
            <label>Nombre:<br>
                <input type="text" name="nombre" required style="width:100%;padding:0.5rem;margin-bottom:1rem;">
            </label>
            <label>Empresa:<br>
                <input type="text" name="empresa" style="width:100%;padding:0.5rem;margin-bottom:1rem;">
            </label>
            <label>Email:<br>
                <input type="email" name="email" required style="width:100%;padding:0.5rem;margin-bottom:1rem;">
            </label>
            <label>Teléfono:<br>
                <input type="text" name="telefono" style="width:100%;padding:0.5rem;margin-bottom:1rem;">
            </label>
            <label>Mensaje:<br>
                <textarea name="mensaje" required rows="4" style="width:100%;padding:0.5rem;margin-bottom:1rem;"></textarea>
            </label>
            <button type="submit" class="btn-principal" style="width:100%;">Enviar</button>
        </form>
        <div style="margin-top:2rem;text-align:center;">
            <p>O escríbenos directamente a <a href="mailto:info@agroconsultora.cl">info@agroconsultora.cl</a> o por WhatsApp: <a href="https://wa.me/56912345678" target="_blank">+56 9 1234 5678</a></p>
        </div>
    </section>
    {footer_html}
</body>
</html>
"""

# Estructura del proyecto
estructura = {
    "agroconsultora-cerezas": [
        ("README.md", contenido_readme),
        ("index.html", contenido_index),
        ("servicios.html", contenido_servicios),
        ("nosotros.html", contenido_nosotros),
        ("proyectos.html", contenido_proyectos),
        ("recursos.html", contenido_recursos),
        ("contacto.html", contenido_contacto),
        ("css/estilos.css", contenido_css),
        ("js/main.js", contenido_js),
        ("assets/img/.gitkeep", ""),       # Archivo vacío para mantener la carpeta en Git
        ("assets/icons/.gitkeep", ""),
    ]
}

def crear_estructura():
    for root, archivos in estructura.items():
        os.makedirs(root, exist_ok=True)
        for archivo, contenido in archivos:
            path = os.path.join(root, archivo)
            carpeta = os.path.dirname(path)
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
            if archivo.endswith(".gitkeep"):
                open(path, "a").close()
            else:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(contenido)
    print("¡Estructura web completa creada exitosamente!")
    print("Recuerda agregar tus imágenes e íconos personalizados en assets/img y assets/icons.")

if __name__ == "__main__":
    crear_estructura()
