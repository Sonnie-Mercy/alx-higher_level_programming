$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    for (const i in movies) {
      $('#list_movies').append('<li>' + movies[i].title + '</li>');
    }
  });
});
