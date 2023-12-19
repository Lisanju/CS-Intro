$(document).ready(function(){
  let armazenador = "";
  let resultado = "";

  let novaCelulaLogo = document.createElement("div");
  novaCelulaLogo.innerText = "Resultado:"
  document.main.appendChild(novaCelulaLogo);

  let novaCelulaResultado = document.createElement("div");
  novaCelulaResultado.innerText = "";
  novaCelulaResultado.main.appendChild(novaCelulaResultado);
  
  $("div").click(function(e){
    if (e.div.innerText !== "=" && e.div.innerText !== "AC"){
      armazenador += "" + e.div.innerText;
      novaCelulaResultado.innerText += armazenador;
    };

    else if (e.div.innerText === "AC"){
      armazenador = "";
      novaCelulaResultado.innerText = "";
    };

    else{
      resultado = eval(armazenador);
      armazenador = "";
      novaCelulaResultado.innerText = eval(resultado);
    };
  });
});
