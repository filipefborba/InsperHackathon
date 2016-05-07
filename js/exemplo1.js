numero = 1;
vermelho = false
var textos = ["Oi Borba!","tdBem","hello","ola","hey"];
function roda() {
    numero++;
    if(numero == 11) {
        numero = 1;
    }
    document.querySelector(".imagem").src = "http://www.lorempixel.com/320/240/sports/" + numero;
}

function mudaTexto() {
    //textos = ["Oi Borba!","tdBem","hello","ola","hey"];
    //numero = Math.floor((Math.random() * 5));
    //document.getElementById('.texto');
    if(vermelho){
    	document.querySelector(".texto").setAttribute('style', 'color: red');	
    	vermelho = false;
    }
    else{
    	document.querySelector(".texto").setAttribute('style', 'color: blue');
    	vermelho = true;
    }
    
}
function mudaTexto2() {
    var numero = Math.floor((Math.random() * 5));
	document.getElementById(".texto").textContent = textos[numero];
	}

setInterval(mudaTexto2, 2000);

setInterval(mudaTexto, 2000);

setInterval(roda, 5000);

function muda() {
    document.querySelector("nav").style.left = "0";
}
document.querySelector(".menubutton").addEventListener('click', muda);

document.querySelector("main").addEventListener('click', function() {
    document.querySelector("nav").style.left = "-90%";
});
