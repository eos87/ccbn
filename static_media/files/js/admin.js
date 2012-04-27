(function($){
    $(document).ready(function(){
        $('.chozen, #id_municipio').chosen({
            allow_single_deselect: true,
        });
        $('.form-row').each(function(index, item){
            $(item).removeClass('form-row').addClass('form-row-fix');
            $(item).append('<div style="clear: both"></div>');
        })
    });
})(jQuery || django.jQuery);