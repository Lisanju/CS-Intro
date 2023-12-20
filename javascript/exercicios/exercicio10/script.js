$(document).ready(function(){
  var carros = [
    {
      "nome": "Gol",
      "fabricante": "Volkswagen",
      "ano": 2009,
      "potencia": 3000,
      "preco": 150000,
      "acessorios": ["banco", "teto", "boneco"]
    },
    {
      "nome": "Mobi",
      "fabricante": "Fiat",
      "ano": 2014,
      "potencia": 4500,
      "preco": 35000,
      "acessorios": ["janela", "pneu-extra", "macaco"]
    },
    {
      "nome": "Onix",
      "fabricante": "Chevrolet",
      "ano": 2019,
      "potencia": 5000,
      "preco": 500000,
      "acessorios": ["asa", "turbo", "espinho"]
    }
  ];

  function adicionarLinha(carro){
    var acessorios = "<ul>;

    $.each(carro.acessorios, function(chave, valor){
      acessorios += "<li>" + acessorio + "</li>";
    });

    acessorios += "</ul>";

    $("#tabelaCarros").append(
      "<tr>" +
        "<td>" + carro.nome + "</td>" +
        "<td>" + carro.fabricante + "</td>" +
        "<td>" + carro.ano + "</td>" +
        "<td>" + carro.potencia + "</td>" +
        "<td>" + carro.preco + "</td>" +
        "<td>" + acessorios + "</td>" +
      "</tr>"
      );
  }

  $.each(carros, function(chave, valor){
    adicionarLinha(valor);
  });
});
