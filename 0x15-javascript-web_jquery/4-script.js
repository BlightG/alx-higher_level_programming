function changeclass () {
  if ($('header.red')[0]) {
    $('header').removeClass('red').addClass('green');
  } else if ($('header.green')[0]) {
    $('header').removeClass('green').addClass('red');
  }
}

$(function () {
  $('#toggle_header').on('click', changeclass);
});
