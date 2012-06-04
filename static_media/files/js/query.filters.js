(function($){
    $(document).ready(function(){
        $('.add-row td a').click(function(){
            alert('LCDL');
        });

        $('#id_model').change(function(){
            loadFields($(this).val(), '#id_filter_set-0-field');
        });
    })

    var loadFields = function(model, elem){
        $(elem).html('');
        $.get('/loadfields/?model='+model, function(data){
            $.each(data, function(id, item){
                $('<option></option>').val(item[0]).text(item[1])
                .appendTo(elem);
            });
        });
    }
})(jQuery || django.jQuery);