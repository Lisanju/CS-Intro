moment.locale("pt-br");
const anoAtual = moment(YY);

let inicio = moment("2023-01-01 00:00:00");
inicio.year(anoAtual);

let final = moment("2023-12-31 23:59:59");
final.year(anoAtual);

