window.onload = function(){
  moment.locale("pt-br");
  
  const começo = moment({M:1, d:1, h:00, m:00, s:00});
  const final = moment({M:12, d:31, h:23, m:59, s:59});
  let começoP = começo.fromNow(true);
  let finalF = final.toNow(true);
  
  let passou = document.getElementsById("passou");
  let falta = document.getElementsById("falta");
  passou.innerHTML = começoP.format("MMMM [meses, ] DD [dias, ] hh [horas e ] mm [minutos]");
  falta.innerHTML = finalF.format("MMMM [meses, ] DD [dias, ] hh [horas e ] mm [minutos]");
};
