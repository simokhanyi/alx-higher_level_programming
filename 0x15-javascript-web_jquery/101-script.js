/* global jQuery */
jQuery(document).ready(function () {
  jQuery('#add_item').click(function () {
    jQuery('<li>Item</li>').appendTo('ul.my_list');
  });

  jQuery('#remove_item').click(function () {
    jQuery('ul.my_list li:last-child').remove();
  });

  jQuery('#clear_list').click(function () {
    jQuery('ul.my_list').empty();
  });
});
