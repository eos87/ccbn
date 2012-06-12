(function($){
    $(document).ready(function(){
        $('#id_municipio, #id_persona, select[id$="libro"]').chosen();
        $('.chozen').not(':hidden').chosen();
        
        $('.add-row td a').click(function(){
            $('.chozen').not(':hidden').chosen();
        });

        $('.form-row').each(function(index, item){
            $(item).removeClass('form-row').addClass('form-row-fix');
            $(item).append('<div style="clear: both"></div>');
        });
    });
})(jQuery || django.jQuery);

function dismissAddAnotherPopup(win, newId, newRepr) {
    var $ = jQuery || django.jQuery;
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem) {
        var elemName = elem.nodeName.toUpperCase();
        if (elemName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
        } else if (elemName == 'INPUT') {
            if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                elem.value += ',' + newId;
            } else {
                elem.value = newId;
            }
        }
    } else {
        var toId = name + "_to";
        elem = document.getElementById(toId);
        var o = new Option(newRepr, newId);
        SelectBox.add_to_cache(toId, o);
        SelectBox.redisplay(toId);
    }
    win.close();
    $(elem).trigger("liszt:updated");
    if(typeof getPrestamoData == 'function'){
        getPrestamoData(elem);
    }
}