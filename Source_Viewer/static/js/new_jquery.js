$(document).ready(function(){

$('#foo').ready(function () {
    $('#loadingMessage').css('display', 'none');
});
$('#foo').load(function () {
    $('#loadingMessage').css('display', 'none');
});
});