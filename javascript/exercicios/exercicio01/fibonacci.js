var n = prompt("Insira um valor N: ");
var num1 = 0;
var num2 = 1;

if(n == 1){
  console.log(0);
}
else if(n == 2){
  console.log(0);
  console.log(1);
}
else{
  console.log(0);
  console.log(1);
  contador = 3;
  while(contador <= n){
    fN = num1 + num2
    num1 = num2;
    num2 = fN;
    contador++;
    console.log(fN);
  }
}
