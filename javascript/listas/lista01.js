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

function pularPrimeiro(str){
    var resultado = str.substring(1);
    console.log(resultado);
    return resultado
}

var gato = "nana gato preto";
pularPrimeiro(gato);

/*Ex 9*/

var pN = "nana";
var sN = "lardapide";

function concatenarN(str1,str2){
    console.log(str1 + " " + str2);
    return str1 + " " + str2;
}

concatenarN(pN,sN);

/*Ex 10*/

var texto = "nikondacurry pi pi pi";

function getDescription(str){
    console.log(str.substring(0,10) + "...");
    return str.substring(0,10) + "...";
}

getDescription(texto);

/*Ex 11*/

let gato = "nana";

function darNome(str){
    console.log(`O gato se chama ${str}`);
    return `O gato se chama ${str}`
};

darNome(gato);

/*Ex 12*/

let nome = "Elisa";
let sobrenome = "Lardapide";

function getFullName(str1,str2){
    return `${str1} ${str2}`;
};

console.log(getFullName(nome,sobrenome));

/*Ex 13*/

function getMultilineString(str){
    return `I am learning JavaScript  
and I found it to be  
quite fun!`;
};

console.log(getMultilineString());

/*Ex 14*/

function renderTableRow(linha,valor){
    return `
            <tr>
                <td>${linha}</td>
                <td>${valor}</td>
            </tr>`;
};

let rr = "baste";
let pb = "mão";

console.log(renderTableRow(rr,pb));

/*Ex 15*/

function capitalize(word){
    return word.at(0).toUpperCase() + word.substring(1).toLowerCase();
};

console.log(capitalize("nANA"));

/*Ex 16*/

function nameVariations(str){
    return `
            <tr>
                <td>Number of characters</td>
                <td>${str.length}</td>
            </tr>
            <tr>
                <td>First character</td>
                <td>${str.at(0)}</td>
            </tr>
            <tr>
                <td>Last character</td>
                <td>${str.at(str.length - 1)}</td>
            </tr>
            <tr>
                <td>Lower case</td>
                <td>${str.toLowerCase()}</td>
            </tr>
            <tr>
                <td>Upper case</td>
                <td>${str.toUpperCase()}</td>
            </tr>
            <tr>
                <td>Capitalize</td>
                <td>${str.at(0).toUpperCase() + str.substring(1).toLowerCase()}</td>
            </tr>`
};

console.log(nameVariations("nana"));

/*Ex 17*/

function convertNumberToString(num){
    return num.toString();
}

console.log(convertNumberToString(7));

/*Ex 18*/

function getNextAge(str){
    return Number.parseInt(str) + 1;
}

console.log(getNextAge(20));

/*Ex 19*/

function getBoxWidth(width){
    return Number.parseInt(width);
}

console.log(getBoxWidth("50px"));

/*Ex 20*/

function getDivisionRemainderBy2(number){
    return number % 2;
}

console.log(getDivisionRemainderBy2(8));

/*Ex 21*/

let count = 0;
count += 1;

console.log(count);

/*Ex 22*/

const ageLimit = 18;
console.log(ageLimit);

/*Ex 23*/

const age = 18;

function canVote(number){
    if (number >= 18){
        return true;
    }
    else{
        return false;
    }
}

console.log(canVote(age));

/*Ex 24*/

function getNextAge(str){
    if (str === ""){
        return 0;
    }
    str = Number.parseInt(str);
    return str + 1;
}

let age = "20";
console.log(getNextAge(age));

/*Ex 25*/

function getDescription(string){
    if (string.length > 10){
        return string.substring(0,10) + "...";
    }
    else{
        return string;
    }
}

console.log(getDescription("nana é uma gatona"));

/*Ex 26*/

function canVote(age){
    return age >= 18;
}

console.log(canVote(20));

/*Ex 27*/

function evenOrOdd(number){
    if (number % 2 === 0){
        return "even";
    }
    return "odd";
}

console.log(evenOrOdd(10));

/*Ex 28*/

function getEmptyArray(){
    array = [];
    return array
}

console.log(getEmptyArray());

/*Ex 29*/

