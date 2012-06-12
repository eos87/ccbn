(function($){
    $(document).ready(function(){
        $('.field-dias_mora > input, .field-fecha_retorno > input').attr('readonly', 'readonly');
        $('select[id$="libro"]').chosen().change(function(){
            var self = this;
            $.get('/getprestamodata/?id='+$(this).val()+'&person='+$('#id_persona').val(), 
                function(data){
                    var fecha_retorno = new Date(data);
                    var fecha_actual = new Date();
                    var mora = Math.ceil((fecha_actual - fecha_retorno)/(1000*60*60*24));
                    var $parent = $(self).parent();
                    if(mora>=0){
                        $parent.siblings('.field-dias_mora').children('input').val(mora);    
                    }else{
                        $parent.siblings('.field-dias_mora').children('input').val(0);
                    }                    
                    $parent.siblings('.field-fecha_retorno').children('input').val(data);
                });
        });
    });
})(jQuery || django.jQuery);