/* global jQuery */
jQuery(document).ready(function () {
  jQuery('#add_item').click(function () {
    jQuery('<li>Item</li>').appendTo('.my_list');
  });
});
