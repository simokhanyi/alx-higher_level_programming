/* global jQuery */
jQuery(document).ready(function () {
  jQuery('#toggle_header').click(function () {
    jQuery('header').toggleClass('red green');
  });
});
