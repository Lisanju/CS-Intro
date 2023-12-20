window.onload = function(){
  moment.locale("pt-br");
  
  const agora = moment();
  const comeco = agora.clone().startOf("year");
  const final = agora.clone().endOf("year");

  const restante = moment.duration(final.diff(agora));
  const passado = moment.duration(agora.diff(comeco));

  function retornarDiferenca(duration){
    const meses = duration.months();
    const dias = duration.days();
    const horas = duration.hours();
    const minutos = duration.minutes();

    const texto = `${meses} meses, ${dias} dias, ${horas} horas e ${minutos} minutos`; 
    return texto
  };
  
  const passou = document.getElementById("passou");
  const falta = document.getElementById("falta");
  passou.innerHTML = retornarDiferenca(passou);
  falta.innerHTML = retornarDiferenca(restante);
