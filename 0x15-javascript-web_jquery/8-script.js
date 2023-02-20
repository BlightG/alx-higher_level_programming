$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function(values) {
      const results = values.results
      $.each(results, function(i, result) {
         $('#list_movies').append('<li>' + result.title+ '</li>');
      });
    }
  });
});
