// Muestra el clima de Santiago en el banner superior
document.addEventListener('DOMContentLoaded', () => {
  const banner = document.getElementById('weather-banner');
  if (!banner) return;

  const locale = document.documentElement.lang.startsWith('es') ? 'es' : 'en';
  const label = locale === 'es' ? 'Clima en Santiago:' : 'Weather in Santiago:';
  const icons = {
    0: '☀️',
    1: '🌤️',
    2: '⛅',
    3: '☁️',
    45: '🌫️',
    48: '🌫️',
    51: '🌦️',
    53: '🌦️',
    55: '🌧️',
    61: '🌧️',
    63: '🌧️',
    65: '🌧️',
    71: '🌨️',
    73: '🌨️',
    75: '❄️',
    80: '🌧️',
    81: '🌧️',
    82: '🌧️',
    95: '⛈️',
    96: '⛈️',
    99: '⛈️'
  };

  const url =
    'https://api.open-meteo.com/v1/forecast?latitude=-33.45&longitude=-70.66&current_weather=true&timezone=auto';

  fetch(url)
    .then(resp => resp.json())
    .then(data => {
      const cw = data.current_weather;
      const icon = icons[cw.weathercode] || '';
      banner.textContent = `${label} ${icon} ${cw.temperature}\u00B0C`;
    })
    .catch(() => {
      banner.textContent = locale === 'es' ? 'Clima no disponible' : 'Weather unavailable';
    });
});
