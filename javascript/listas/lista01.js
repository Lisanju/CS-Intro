/*Ex 1*/
function soma(a,b){
  console.log(a+b);
  return a+b;
};

soma(1,3);

/*Ex 2*/

function mult(a,b){
  console.log(a*b);
  return a*b;
};

mult(3,2);

/*Ex 3*/

function medirTamanho(str){
    console.log(str.length);
    return str.length;
}

medirTamanho("nana");

/*Ex 4*/

function gritarNome(name){
    console.log(name.toUpperCase());
    return name.toUpperCase();
}

gritarNome("nana");

/*Ex 5*/

function falaBaixo(name){
    console.log(name.toLowerCase());
    return name.toLowerCase();
}

falaBaixo("NANA");

/*Ex 6*/

function primeiroChar(str){
    var primeiro = str[0];
    console.log(primeiro);
    return primeiro;
}

var gato = "nana";
primeiroChar(gato);

/*Ex 7*/

function ultimoChar(str){
    var ultimo = str.at(-1);
    console.log(ultimo);
    return ultimo;
}

var gato = "nana";
ultimoChar(gato);

/*Ex 8*/
