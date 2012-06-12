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
})(jQuery || django.jQuery);