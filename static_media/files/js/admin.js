(function($){
    $(document).ready(function(){
        $('#id_municipio').chosen();
        $('.chozen').not(':hidden').chosen();
        
        $('.add-row td a').click(function(){
            $('.chozen').not(':hidden').chosen();
        });

        $('.form-row').each(function(index, item){
            $(item).removeClass('form-row').addClass('form-row-fix');
            $(item).append('<div style="clear: both"></div>');
        })
    });
})(jQuery || django.jQuery);