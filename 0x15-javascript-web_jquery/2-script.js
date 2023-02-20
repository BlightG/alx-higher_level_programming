function myfunction () {
  $('header').css('color', '#FF0000');
}

$(function () {
  $('#red_header').on('click', myfunction);
});
