//JavaScript Document

'use strict'

var flag = 'p0'

function con(i) {
    document.getElementById(flag).style.display = 'none';
    document.getElementById('p' + i).style.display = 'inline';
    flag = 'p' + i
}