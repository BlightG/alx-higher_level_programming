$(function () {
  $('#add_item').on('click', function () {
    $('ul.my_list').prepend('<li>Item</li>');
  });
});
