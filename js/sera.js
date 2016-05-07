$(".titu").hide();
$(".calendario").hide();
$("splash").show();
$("select").change(function() {
$(".splash").hide();
$(".calendario").show();
$(".titu").show();
});
