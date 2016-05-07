numero = 1;

function roda() {
    numero++;
    if(numero == 11) {
        numero = 1;
    }
    $(".imagem").attr("src", "http://www.lorempixel.com/320/240/sports/" + numero);
}

setInterval(roda, 5000);

function muda() {
    $("nav").css("left", "0");
}
$(".menubutton").click(muda);

$("main").click(function() {
    $("nav").css("left", "-90%");
});
