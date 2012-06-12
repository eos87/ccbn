(function($){
    $(document).ready(function(){
        $('select[id$="libro"]').chosen().change(function(){
            getPrestamoData($(this));            
        });
    });
})(jQuery || django.jQuery);

var getPrestamoData = function(elem){
    var $ = jQuery || django.jQuery;
    
}