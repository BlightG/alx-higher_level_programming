function myfunction () {
  $('header').addClass('red');
}

$(function () {
  $('#red_header').on('click', myfunction);
});
