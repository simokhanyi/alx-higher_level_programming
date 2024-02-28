/* global jQuery */
jQuery(document).ready(function () {
  function fetchTranslation () {
    const languageCode = jQuery('#language_code').val();
    jQuery.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      jQuery('#hello').text(data.hello);
    });
  }

  jQuery('#btn_translate').click(fetchTranslation);

  jQuery('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key code
      fetchTranslation();
    }
  });
});
