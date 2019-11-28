//JavaScript Document

'use strict'

function type() {
    var str = document.getElementsByTagName('code')[0].innerHTML.toString();
    var i = 0;
    document.getElementsByTagName('code')[0].innerHTML = '';

    setTimeout(function() {
        var se = setInterval(function() {
            i++;
            document.getElementsByTagName('code')[0].innerHTML = str.slice(0, i) + '|';
            if (i == str.length) {
                clearInterval(se);
                document.getElementsByTagName('code')[0].innerHTML = str;
            }
        }, 0)
    }, 0)
}

type()