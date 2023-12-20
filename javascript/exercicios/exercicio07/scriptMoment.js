window.onload = function(){
  moment.locale("pt-br");
  
  const agora = moment(); // momento atual
  
  const começo = moment({M:1, d:1, h:00, m:00, s:00});
  const final = moment({M:12, d:31, h:23, m:59, s:59});
  
  let começoP = agora.diff(começo, 'seconds');
  let finalF = final.diff(agora, 'seconds');
  
  começoP = moment.duration(começoP);
  finalF = moment.duration(finalF);
  
  let passou = document.getElementById("passou");
  let falta = document.getElementById("falta");
  
  passou.innerHTML = começoP.format("MMMM [meses, ] DD [dias, ] hh [horas e ] mm [minutos]");
  falta.innerHTML = finalF.format("MMMM [meses, ] DD [dias, ] hh [horas e ] mm [minutos]");
};
