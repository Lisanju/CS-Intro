# --------------------- Exercício 10.1 --------------------- #

vetor <- c(2,4,6,8,10) # valores em um vetor fornecido pelo usuário #

med_aritmetica <- function(a){
  soma <- 0
  for (x in a){
    soma = soma + x
  }
  soma / length(a)
  
}

med_aritmetica(vetor) # retorna 6 #
mean(vetor) # retorna 6 #

# --------------------- Exercício 10.2 --------------------- #

c_to_f <- function(c){
  (c * 1.8) + 32
}

f_to_c <- function(f){
  (f - 32) / 1.8
}

c_to_f(27) # retorna 80.6 #
f_to_c(80.6) # retorna 27 #

# --------------------- Exercício 10.3 --------------------- #

temp_conv <- function(temp,f_to){
  if (f_to == TRUE){
    (temp * 1.8) + 32
  }
  else{
    (temp - 32) / 1.8
  }
}

temp_conv(27,TRUE) # retorna 80.6 - Celsius para Fahrenheit #
temp_conv(80.6,FALSE) # retorna 27 - Fahrenheit para Celsius #
