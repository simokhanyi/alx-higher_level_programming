/* global jQuery */
jQuery(document).ready(function () {
  jQuery.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    jQuery('#character').text(data.name);
  });
});
