$(document).ready(function(){

  var linhaNome = $("#nome");
  var linhaFabricante = $("#fabricante");
  var linhaAno = $("#ano");
  var linhaPotencia = $("#potencia");
  var linhaPreco = $("#preco");
  var linhaAcessorios = $("#acessorios");

  
  
  function tratamento(dados){
    $.each(dados, function(chave, valor){
      
    });
  };
  
  $.getJSON("carros.json", tratamento);
});
