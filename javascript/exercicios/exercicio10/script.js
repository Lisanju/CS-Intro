$(document).ready(function(){

  var linhaNome = $("#nome");
  var linhaFabricante = $("#fabricante");
  var linhaAno = $("#ano");
  var linhaPotencia = $("#potencia");
  var linhaPreco = $("#preco");
  var linhaAcessorios = $("#acessorios");
  
  function tratamento(dados){
    $.each(dados, function(chave, valor){
      let td = $("<td>");
      td.html(valor);
      if (chave === "nome"){
        linhaNome.append(td);
      } else {
        if (chave === "fabricante"){
          linhaFabricante.append(td);
        } else {
          if (chave === "ano"){
            linhaAno.append(td);
          } else {
            if (chave === "potencia"){
              linhaPotencia.append(td);
            } else {
              if (chave === "preco"){
                linhaPreco.append(td);
              } else {
                let ul = $("<ul>");
                let li = $("<li>");
                for (let i = 0; i < valor.length; i++){
                li.html(valor[i]);
                ul.append(li);
                }
              }
            }
          }
        }
      }
    });
  };
  $.getJSON("carros.json", tratamento);
});
