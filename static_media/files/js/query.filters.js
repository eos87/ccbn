(function($){
    var url;
    $(document).ready(function(){
        url = window.location.href.split('/');
        state = (url[url.length-2] == 'add') ? 'add' : 'edit';

        if( state == 'edit' ){
            id = url[url.length-2];
            var combos = $('.field-field > select');
            loadFields($('#id_model').val(), '.field-field > select');
            $.getJSON('/getfilters/?id='+id, function(data){
                $.each(data, function(id, item){
                    $(combos[id]).val(item.field);
                });
            });
        }else{
            if($('#id_model').val() != ''){
                loadFields($('#id_model').val(), '.field-field > select');
            }
        }

        // $('.add-row td a').click(function(){
        //     alert('LCDL');
        // });

        $('#id_model').change(function(){
            loadFields($(this).val(), '.field-field > select');
        });
    });  
    

    var loadFields = function(model, elem){
        $(elem).html('');
        $.get('/loadfields/?model='+model, function(data){
            $('<option></option>').val('').text('---------').appendTo(elem);
            $.each(data, function(id, item){
                $('<option></option>').val(item[0]).text(item[1])
                .appendTo(elem);
            });
        });
    }
})(jQuery || django.jQuery);