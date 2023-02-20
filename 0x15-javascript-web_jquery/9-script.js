$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    crossDomain: true,
    xhrFields: {
        withCredentials: true
    },
    headers: {
              "accept": "application/json",
              "Access-Control-Allow-Origin":"https://fourtonfish.com/hellosalut/?lang=fr",
              "Access-Control-Allow-Methods":"GET, POST, PATCH, PUT, DELETE, OPTIONS",
              'Access-Control-Allow-Headersi':' Origin, Content-Type, X-Auth-Token'
          },
    success: function(value) {
      $('#hello').text(value.hello);
    }
  });
});
