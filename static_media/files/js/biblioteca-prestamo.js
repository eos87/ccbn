(function($){
    $(document).ready(function(){
        $('.field-fecha_retorno input').attr('readonly', 'readonly');
        $('input[id$="dias"]').keyup(function(){
            var d = new Date();
            var days = $(this).val();
            if (/^\d+$/.test(days)){
                d.setDate(d.getDate()+parseInt(days));
                var new_date = d.getDate()+"/"+(d.getMonth()+1)+"/"+d.getFullYear();
                $(this).parent().siblings('.field-fecha_retorno').children('input').val(new_date);
            }else{
                $(this).parent().siblings('.field-fecha_retorno').children('input').val('');
            }
        });
    });
    $(window).load(function(){
        var $launcher = $($('.field-fecha .datetimeshortcuts').children()[0]);
        $launcher.attr('href', 'javascript:keyupTrigger();');
    });
})(jQuery || django.jQuery);

var keyupTrigger = function(key){
    key = typeof key !== 'undefined' ? false : true;
    var $ = jQuery || django.jQuery;
    if(key){
        DateTimeShortcuts.handleCalendarQuickLink(0, 0);    
    }
    $('#id_prestamo_set-0-dias').trigger('keyup');
}