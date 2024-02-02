document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(Response => Response.json())
    .then(data => {
      document.getElementById('character').textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching:', error);
    });
});
