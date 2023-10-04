$.ajax({
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	method: 'GET',
	dataType: 'json',
	success: function(data {
		$.each(data.results, function(index, movie) {
			$('<li>').text(movie.title).appendTo('UL#list_movies');
		}
	});
});
