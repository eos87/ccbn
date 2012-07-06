(function( $ ){
    $.fn.progressChart = function( options ){
        var settings = $.extend( {
              'meta'            : 100,
              'reached'         : 25,
              'parent_color'    : 'yellow, #df803d',
              'height'          : '75px',
              'font_size'       : '22px',
              'symbol'          : ''
            }, options);

        this.css({
            'padding'       : '20px',
            'background'    : '#F3F3F3'
        });

        var $chart = $('<div></div>');
        // set style to parent div
        $chart.css({
            'width'         : '100%',
            'height'        : settings.height,
            'background'    : 'linear-background(top, '+settings.parent_color+')',
            'position'  : 'relative'
        });

        // set child with reached goal
        var $child = $('<div></div>');
        var $text = $('<div></div>'); // reached label
        var $meta = $('<div></div>'); // meta label
        var alcanzado = ((settings.reached*100)/settings.meta).toFixed(0);
        var color = '#df613a, #df2d4d';
        var lbl_reached = '';

        // set correct color according to amount reached 
        if(alcanzado <= 25){
            color = '#df613a, #df2d4d';
        }else if(alcanzado > 25 && alcanzado <= 50){
            color = '#df5d27, #dfa21b';
            lbl_reached = 'Alcanzado: ';
        }else if(alcanzado > 50 && alcanzado <= 75){
            color = '#df9b2d, #dfaa16';
            lbl_reached = 'Alcanzado: ';
        }else if(alcanzado > 75 && alcanzado <= 95){
            color = 'yellow, #df803d';
            lbl_reached = 'Casi listo: ';
        }else{
            color = '#0bad2e, #55df1e';
            lbl_reached = 'Completado: ';
        }

        // verificando que lo alcanzado no supere la meta
        if (settings.reached >= settings.meta){
            var val_reached = 100;
            lbl_reached = 'Sobrepasada: ';
        }else{
            var val_reached = (settings.reached*100)/settings.meta;
        }

        // set attributes to reached label
        $text.css({
            'position'          : 'absolute',
            'right'             : '5px',
            'font-size'         : '14px',
            'font-weight'       : 'bold'
        })
        .text(lbl_reached+settings.reached+settings.symbol);

        $child.css({
            'width'         : val_reached+'%',
            'position'      : 'relative',
            'background'    : 'linear-background(top, '+color+')',
            'height'        : settings.height,
            'line-height'   : settings.height,
            'color'         : '#fff'
        }).append($text);

        // setting gradient according to browser
        if(bowser.firefox){
            $chart.css({'background': '-moz-linear-gradient(top, '+settings.parent_color+')'});
            $child.css({'background': '-moz-linear-gradient(top, '+color+')'});
        }
        if(bowser.webkit){
            $chart.css({'background': '-webkit-linear-gradient(top, '+settings.parent_color+')'});
            $child.css({'background': '-webkit-linear-gradient(top, '+color+')'});
        }
        if(bowser.opera){
            $chart.css({'background': '-o-linear-background(top, '+settings.parent_color+')'});
            $child.css({'background': '-o-linear-background(top, '+color+')'});
        }
        if(bowser.msie && bowser.version >= 10){
            $chart.css({'background': '-ms-linear-background(top, '+settings.parent_color+')'});
            $child.css({'background': '-ms-linear-background(top, '+color+')'});    
        }

        // adding child chart to parent chart
        $child.appendTo($chart);
        // adding meta text
        $meta.css({
            'position'          : 'absolute',
            'right'             : '0px',
            'font-size'         : '12px'
        }).text('Meta: '+settings.meta+settings.symbol).appendTo($chart);

        $chart.appendTo(this);
    }
})( jQuery );