/* global jQuery */
jQuery(document).ready(function () {
  jQuery('#btn_translate').click(function () {
    const languageCode = jQuery('#language_code').val();
    jQuery.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      jQuery('#hello').text(data.hello);
    });
  });
});
