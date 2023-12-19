$(document).ready(function(){
  const main = document.getElementsByTagName("main");
  let armazenador = "";
  let resultado = "";

  let novaCelulaLogo = $("<div>").text("Resultado:");
  $("main").append(novaCelulaLogo);

  let novaCelulaResultado = $("<div>").text("");
  $("main").append(novaCelulaResultado);
  
  $("div").click(function(e){
    if ($(this).text() !== "=" && $(this).text() !== "AC"){
      armazenador += "" + $(this).text();
      novaCelulaResultado.innerText += armazenador;
    };

    else if ($(this).text() === "AC"){
      armazenador = "";
      novaCelulaResultado.innerText = "";
    };

    else{
      resultado = eval(armaEzenador);
      armazenador = "";
      novaCelulaResultado.innerText = resultado;
    };
  });
});
