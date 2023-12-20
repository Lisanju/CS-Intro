$(document).ready(function(){

  function tratamento(dados){
    $.each(dados, function(chave, valor){
      console.log("O valor de " + chave + " é " + valor);
    });
  };
  
  $.getJSON("carros.json", tratamento);
});
