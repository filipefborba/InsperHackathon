firebase = new Firebase("https://33ac8ed52a54d63548c078d3545d7e66.firebaseio.com/");

firebase.child("moto").on("value", function(snapshot) {
	var numero = Math.floor((Math.random() * 5));
    $(".valor").text(snapshot.val()[numero]);
});

$(".link").click(function() {
    firebase.set({"moto": ["Hackathon!","Sábado!","Não perca!"]});
});