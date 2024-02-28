/* global jQuery */
jQuery(document).ready(function () {
  jQuery.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    jQuery('#hello').text(data.hello);
  });
});
