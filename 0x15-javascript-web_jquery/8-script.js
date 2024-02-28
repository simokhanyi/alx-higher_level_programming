/* global jQuery */
jQuery(document).ready(function () {
  jQuery.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    jQuery.each(data.results, function (index, movie) {
      jQuery('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
