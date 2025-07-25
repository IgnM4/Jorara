// Carga el clima actual de las capitales regionales de Chile usando Open-Meteo
export async function loadChileWeather() {
  const capitals = [
    { city: "Arica", region: "Arica y Parinacota", lat: -18.4783, lon: -70.3211 },
    { city: "Iquique", region: "Tarapac\u00e1", lat: -20.2133, lon: -70.1519 },
    { city: "Antofagasta", region: "Antofagasta", lat: -23.65, lon: -70.4 },
    { city: "Copiap\u00f3", region: "Atacama", lat: -27.3667, lon: -70.3333 },
    { city: "La Serena", region: "Coquimbo", lat: -29.9045, lon: -71.2489 },
    { city: "Valpara\u00edso", region: "Valpara\u00edso", lat: -33.0458, lon: -71.6197 },
    { city: "Santiago", region: "Metropolitana", lat: -33.4489, lon: -70.6693 },
    { city: "Rancagua", region: "O'Higgins", lat: -34.169, lon: -70.7406 },
    { city: "Talca", region: "Maule", lat: -35.4333, lon: -71.6667 },
    { city: "Chill\u00e1n", region: "\u00d1uble", lat: -36.6067, lon: -72.1034 },
    { city: "Concepci\u00f3n", region: "Biob\u00edo", lat: -36.827, lon: -73.0498 },
    { city: "Temuco", region: "La Araucan\u00eda", lat: -38.7359, lon: -72.5904 },
    { city: "Valdivia", region: "Los R\u00edos", lat: -39.8142, lon: -73.2459 },
    { city: "Puerto Montt", region: "Los Lagos", lat: -41.4717, lon: -72.9369 },
    { city: "Coyhaique", region: "Ays\u00e9n", lat: -45.5752, lon: -72.0662 },
    { city: "Punta Arenas", region: "Magallanes", lat: -53.1638, lon: -70.9171 }
  ];

  const codeMap = {
    0: 'Despejado',
    1: 'Mayormente despejado',
    2: 'Parcialmente nublado',
    3: 'Nublado',
    45: 'Neblina',
    48: 'Neblina',
    51: 'Llovizna ligera',
    53: 'Llovizna',
    55: 'Llovizna intensa',
    61: 'Lluvia ligera',
    63: 'Lluvia moderada',
    65: 'Lluvia fuerte',
    71: 'Nevada ligera',
    73: 'Nevada',
    75: 'Nevada intensa',
    80: 'Chubascos ligeros',
    81: 'Chubascos',
    82: 'Chubascos fuertes',
    95: 'Tormenta',
    96: 'Tormenta con granizo',
    99: 'Tormenta con granizo'
  };

  const container = document.getElementById('weather-cards');
  if (!container) return;
  container.innerHTML = '';

  for (const cap of capitals) {
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${cap.lat}&longitude=${cap.lon}&current_weather=true&timezone=auto`;
    try {
      const resp = await fetch(url);
      const data = await resp.json();
      const cw = data.current_weather;
      const desc = codeMap[cw.weathercode] || 'N/A';
      const card = document.createElement('div');
      card.className = 'weather-card fade-in';
      card.innerHTML = `<h3>${cap.city}</h3><p>${cw.temperature}\u00b0C</p><p>${desc}</p>`;
      container.appendChild(card);
    } catch (err) {
      const card = document.createElement('div');
      card.className = 'weather-card fade-in';
      card.innerHTML = `<h3>${cap.city}</h3><p>No disponible</p>`;
      container.appendChild(card);
    }
  }

  const cards = container.querySelectorAll('.fade-in');
  cards.forEach((el, i) => {
    setTimeout(() => el.classList.add('visible'), 300 + i * 100);
  });
}

document.addEventListener('DOMContentLoaded', loadChileWeather);
