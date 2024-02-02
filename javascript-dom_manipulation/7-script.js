document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(Response => Response.json())
  .then(data => {
    const movieList = document.getElementById('list_movies');
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      movieList.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching:', error);
  })
});

