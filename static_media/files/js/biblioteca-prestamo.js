(function($){
    $(document).ready(function(){
        $('.field-fecha_retorno input').attr('readonly', 'readonly');
        $('input[id$="dias"]').keyup(function(){
            var foo = $('#id_fecha_0').val().split('/');
            var d = new Date(foo[1] + '/' + foo[0] + '/' + foo[2]);
            var days = $(this).val();
            if (/^\d+$/.test(days)){
                d.setDate(d.getDate()+parseInt(days));
                var new_date = d.getDate()+"/"+(d.getMonth()+1)+"/"+d.getFullYear();
                $(this).parent().siblings('.field-fecha_retorno').children('input').val(new_date);
            }else{
                $(this).parent().siblings('.field-fecha_retorno').children('input').val('');
            }
        });
        $('#id_fecha_0').keyup(function(){
            keyupTrigger(false);
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