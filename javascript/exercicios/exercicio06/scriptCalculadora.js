$(document).ready(function(){
  const main = document.getElementsByTagName("main");
  let armazenador = "";
  let resultado = "";

  let novaCelulaLogo = document.createElement("div");
  novaCelulaLogo.innerText = "Resultado:"
  document.main.appendChild(novaCelulaLogo);

  let novaCelulaResultado = document.createElement("div");
  novaCelulaResultado.innerText = "";
  novaCelulaResultado.main.appendChild(novaCelulaResultado);
  
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
