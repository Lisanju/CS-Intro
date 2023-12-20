$(document).ready(function(){
  function obterTamanho(){
    return parseFloat($("p").css("font-size"));
  };
  
  $("#fMais").click(function(e){
    $("p").attr("font-size", obterTamanho() + 1);
  });

  $("#fMenos").click(function(e){
    $("p").attr("font-size", obterTamanho() - 1);
  });
});
