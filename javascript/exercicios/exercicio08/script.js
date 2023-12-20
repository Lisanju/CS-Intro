$(document).ready(function(){
  function obterTamanho(){
    return parseFloat($("p").css("font-size"));
  };
  
  const aumentar = $("#fMais");
  const diminuir = $("#fMenos");
  const noturno = $("#mNoturno");
  const diurno = $("#mDiurno");

  aumentar.on("click", function(){
    $("p").css("font-size", obterTamanho() + 1);
  });

  diminuir.on("click", function(){
    $("p").css("font-size", obterTamanho() - 1);
  });

  noturno.on("click", function(){
    $("body").css("background-color", "black");
    $("p").css("color", "white");
  })

  diurno.on("click", function(){
    $("body").css("background-color", "white");
    $("p").css("color", "black");
  })
});
