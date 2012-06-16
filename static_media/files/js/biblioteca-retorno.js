(function($){
    $(document).ready(function(){
        $('.field-dias_mora > input, .field-fecha_retorno > input').attr('readonly', 'readonly');
        $('select[id$="libro"]').chosen().change(function(){
            var self = this;
            $.get('/getprestamodata/?id='+$(this).val()+'&person='+$('#id_persona').val(), 
                function(data){
                    var fecha_retorno = new Date(data);
                    var fecha = $('#id_fecha_0').val();
                    fecha = fecha.split('/')
                    fecha = fecha[1] + '/' + fecha[0] + '/' + fecha[2];
                    var fecha_actual = new Date(fecha);
                    var mora = Math.ceil((fecha_actual - fecha_retorno)/(1000*60*60*24));
                    var $parent = $(self).parent();
                    if(mora>=0){
                        $parent.siblings('.field-dias_mora').children('input').val(mora);    
                    }else{
                        $parent.siblings('.field-dias_mora').children('input').val(0);
                    }                    
                    $parent.siblings('.field-fecha_retorno').children('input').val(fecha_retorno.getDate()+'/'
                        +(fecha_retorno.getMonth()+1)+'/'+fecha_retorno.getFullYear());
                });
        });
        $('#id_fecha_0').keyup(function(){
            stateListener(false);
        });
    });
    $(window).load(function(){
        var $launcher = $($('.field-fecha .datetimeshortcuts').children()[0]);
        $launcher.attr('href', 'javascript:stateListener();');
    });    
})(jQuery || django.jQuery);

var stateListener = function(cal){
    cal = typeof cal !== 'undefined' ? false : true;
    var $ = jQuery || django.jQuery;
    if(cal){
        DateTimeShortcuts.handleCalendarQuickLink(0, 0);    
    }
    $('#id_retorno_set-0-libro').trigger('change');
}