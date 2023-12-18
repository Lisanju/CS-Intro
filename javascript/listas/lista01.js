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
    const array = [];
    return array
}

console.log(getEmptyArray());

/*Ex 29*/

function getNumberOfElements(array){
    return array.length;
}

const gatos = ["tom","nana","brisa","salem"];

console.log(getNumberOfElements(gatos));

/*Ex 30*/

const apps = [];

function useCalculator(array){
    array.push("Calculator");
    return array;
}

console.log(useCalculator(apps));

/*Ex 31*/

function useApp(apps,app){
    apps.push(app);
    return apps;
}

const apps = [];
console.log(useApp(apps,"sonok"));

/*Ex 32*/

function getFirstApp(array){
    return array[0];
}

apps = ["sonok","manek","tilap"];
console.log(getFirstApp(apps));

/*Ex 33*/

function getLastApp(array){
    return array.at(-1);
}

apps = ["sonok","manek","tilap"];
console.log(getLastApp(apps));

/*Ex 34*/

function loopThroughElements(array){
    array.forEach(function(element){
       console.log(element); 
    });
}

const gatos = ["nana","tom","salem","brisa"];
console.log(loopThroughElements(gatos));

/*Ex 35*/

function logUserIds(array){
    array.forEach(function(element){
        console.log(element);
    })
}

userIds = [0,3,5,6,7];
logUserIds(userIds);

/*Ex 36*/

function sumGrades(grades){
    let sum = 0
    grades.forEach(function(grade){
        sum += grade;
    })
    console.log(sum);
    return sum;
}

const grades = [7,10,6];
sumGrades(grades);

/*Ex 37*/

function sumPositiveNumbers(numbers){
    let sum = 0;
    numbers.forEach(function(number){
        if (number > 0){
            sum += number;
        }
    });
    return sum;
}

numbers = [-1,-2,-3,-4,5,6];
console.log(sumPositiveNumbers(numbers));

/*Ex 38*/

function sumOddNumbers(numbers){
    let sum = 0;
    numbers.forEach(function(number){
        if (number % 2 !== 0){
            sum += number;
        }
    });
    return sum;
}

numbers = [1,2,3,4,5,6,7,8,9,10];
console.log(sumOddNumbers(numbers));

/*Ex 39*/

function getDropdown(countries){
    let html = `<option value="">Please select</option>`;
    countries.forEach(function(country){
        console.log(country);
        html += `<option value="${country.toLowerCase()}">${country.at(0).toUpperCase() + country.substring(1).toLowerCase()}</option>`;
    });
    return html;
}

const countries = ["Brazil","Russia","Spain","Netherlands"];

console.log(getDropdown(countries));

/*Ex 40*/

function renderTableRows(rows){
    let html = ``;
    rows.forEach(function(row){
        console.log(row);
        html += `<tr>
                    <td>${row[0]}</td>
                    <td>${row[1]}</td>
                </tr>`
    });
    return html;
}

rows = [["Carbs", "17g"], ["Protein", "19g"], ["Fat", "5g"]];

console.log(renderTableRows(rows));

/*Ex 41*/

function getPositiveTemperatures(temperatures){
    const positiveTemperatures = temperatures.filter(function(temperature){
        return temperature > 0;
    })
    return positiveTemperatures;
}

const temperatures = [-30,-5,-1,5,18,28,36];
console.log(getPositiveTemperatures(temperatures));

/*Ex 42*/

function getFreezingTemperatures(temperatures){
    const freezingTemperatures = temperatures.filter(function(temperature){
        return temperature <= 0;
    })
    return freezingTemperatures;
}

const temperatures = [-30,-5,-1,5,18,28,36];
console.log(getFreezingTemperatures(temperatures));

/*Ex 43*/

function getYear(years,searchYear){
    let year = years.find(function(year){
        return year === searchYear;
    })
    return year;
}

const years = [2020,2021,2022,2023,2024];
console.log(getYear(years,2023));

/*Ex 44*/

function getOddYears(years){
    let year = years.filter(function(year){
        return year % 2 !== 0;
    })
    return year;
}

const years = [2020,2021,2022,2023,2024];
console.log(getOddYears(years));

/*Ex 45*/

function isAppUsed(apps,app){
    return apps.includes(app)
}

/*Ex 46*/

function getStringSizes(strings){
    let stringSizes = strings.map(function(string){
        return string.length;
    })
    return stringSizes;
}

const strings = ["nana","tom"]
console.log(getStringSizes(strings));

/*Ex 47*/

