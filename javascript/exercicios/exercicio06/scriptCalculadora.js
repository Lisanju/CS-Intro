$(document).ready(function(){
  let armazenador = "";
  let resultado = "";
  
  $("div").click(function(e){
    if (e.div.innerText !== "=" && e.div.innerText !== "AC"){
      armazenador += e.div.innerText;
    };

    else if (e.div.innerText === "AC"){
      armazenador = "";
    };

    else{
      resultado = eval(armazenador);
      armazenador = "";
      
      return resultado;
    };
  });
});
