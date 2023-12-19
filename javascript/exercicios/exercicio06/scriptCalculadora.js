$(document).ready(function(){
  let armazenador = "";
  let resultado = "";
  
  $("div").click(function(e){
    if (e.div !== "=" && e.div !== "AC"){
      armazenador += e.div;
    };

    else if (e.div === "AC"){
      armazenador = "";
    };

    else{
      resultado = eval(armazenador);
      armazenador = "";
      
      return resultado;
    };
  });
});
