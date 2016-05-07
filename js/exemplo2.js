nav = $("nav");
nav.css("left", "0");
nav.hide();
$(".menubutton").click(function() {
    nav.show(500);
});
$("main").click(function() {
    nav.hide(500);
});
