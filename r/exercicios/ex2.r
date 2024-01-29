# ======================= Capítulo 11 ======================= #

adivinhe <- function() {
  sorteado <- sample.int(10, size=1)
  terminar <- F
  while(terminar == F) {
    palpite <- readline("Seu palpite: ")
    palpite <- as.numeric(palpite)
    if (palpite == sorteado) {
      cat("Acertou.")
      terminar <- T
    } else if (palpite < sorteado) {
      cat("Tente um número maior.")
    } else {
      cat("Tente um número menor.")
    }
  }
}


adivinhe()

# --------------------- Exercício 11.1 --------------------- #

adivinhe <- function() {
  sorteado <- sample.int(10, size=1)
  terminar <- F
  while(terminar == F) {
    palpite <- readline("Seu palpite: ")
    palpite <- as.numeric(palpite)
    if (palpite > 0 & palpite <= 10){
      if (palpite == sorteado) {
        cat("Acertou.")
        terminar <- T
      } else if (palpite < sorteado) {
        cat("Tente um número maior.")
      } else {
        cat("Tente um número menor.")
      }
    }
    else{
      cat("Seu palpite está fora do intervalo.")
    }
  }
}

adivinhe()
# --------------------- Exercício 11.2 --------------------- #

adivinhe <- function() {
  sorteado <- sample.int(10, size=1)
  terminar <- F
  while(terminar == F) {
    palpite <- readline("Seu palpite: ")
    palpite <- as.numeric(palpite)
    palpite <- as.integer(palpite)
    if (palpite > 0 & palpite <= 10){
      if (palpite == sorteado) {
        cat("Acertou.")
        terminar <- T
      } else if (palpite < sorteado) {
        cat("Tente um número maior.")
      } else {
        cat("Tente um número menor.")
      }
    }
    else{
      cat("Seu palpite está fora do intervalo.")
    }
  }
}

adivinhe()

# --------------------- Exercício 11.3 --------------------- #

adivinhe <- function() {
  sorteado <- sample.int(10, size=1)
  terminar <- F
  while(terminar == F) {
    palpite <- readline("Seu palpite: ")
    palpite <- as.numeric(palpite)
    palpite <- as.integer(palpite)
    if (is.na(palpite) == TRUE){
      cat("Você deve usar apenas números para palpitar.")
    }
    else{
      if (palpite > 0 & palpite <= 10){
        if (palpite == sorteado) {
          cat("Acertou.")
          terminar <- T
        } else if (palpite < sorteado) {
          cat("Tente um número maior.")
        } else {
          cat("Tente um número menor.")
        }
      }
      else{
        cat("Seu palpite está fora do intervalo.")
      }
    }
  }
}

adivinhe()

# --------------------- Exercício 11.4 --------------------- #

adivinhe <- function(a,b) {
  sorteado <- sample.int(b, size=1)
  terminar <- F
  while(terminar == F) {
    palpite <- readline("Seu palpite: ")
    palpite <- as.numeric(palpite)
    palpite <- as.integer(palpite)
    if (is.na(palpite) == TRUE){
      cat("Você deve usar apenas números para palpitar.")
    }
    else{
      if (palpite >= a & palpite <= b){
        if (palpite == sorteado) {
          cat("Acertou.")
          terminar <- T
        } else if (palpite < sorteado) {
          cat("Tente um número maior.")
        } else {
          cat("Tente um número menor.")
        }
      }
      else{
        cat("Seu palpite está fora do intervalo.")
      }
    }
  }
}

adivinhe(1,10)

# --------------------- Exercício 11.5 --------------------- #

adivinhe <- function(a,b) {
  sorteado <- sample.int(b, size=1)
  repeat {
    palpite <- readline("Seu palpite: ")
    palpite <- as.numeric(palpite)
    palpite <- as.integer(palpite)
    if (is.na(palpite) == TRUE){
      cat("Você deve usar apenas números para palpitar.")
    }
    else{
      if (palpite >= a & palpite <= b){
        if (palpite == sorteado) {
          cat("Acertou.")
          break
        } else if (palpite < sorteado) {
          cat("Tente um número maior.")
        } else {
          cat("Tente um número menor.")
        }
      }
      else{
        cat("Seu palpite está fora do intervalo.")
      }
    }
  }
}

adivinhe(1,10)

# --------------------- Exercício 11.6 --------------------- #

# Declaração da função com dois parâmetros (a,b)
adivinhe <- function(a,b) {
  
  # Criação de um sample com size igual a 1 a partir do dado de entrada
  # fornecido pelo usuário no parâmetro b, 
  sorteado <- sample.int(b, size=1)
  
  # Estrutura de repetição para que o programa rode até que o usuário
  # acerte o número escolhido pelo programa
  repeat {
    
    # Uso da função readline para coletar um dado de entrada do usuário
    # a partir das teclas a serem digitadas no teclado
    palpite <- readline("Seu palpite: ")
    
    # Como todo dado retornado pela função readline é do tipo character,
    # usamos a função as.numeric para converter em número
    palpite <- as.numeric(palpite)
    
    # Aqui especificamos que o número convertido precisa ser, na verdade,
    # do tipo inteiro
    palpite <- as.integer(palpite)
    
    # Aplicamos a função is.na() para conferir caso o usuário tenha
    # fornecido uma letra ou símbolo em readline, visto que se esse for o caso,
    # será retornado o valor TRUE da função, assim identificando a presença de NAs
    if (is.na(palpite) == TRUE){
      
      # Escrevemos uma mensagem para o usuário avisando que ele deve usar apenas 
      # números, caso is.na() retorne TRUE
      cat("Você deve usar apenas números para palpitar.")
    }
    
    # Caso is.na() retorne FALSE, isto é, no caso de else, prosseguimos com
    # o jogo.
    else{
      
      # Delimitamos que o palpite do jogador precisa estar dentro dos limites
      # fornecidos pelos parâmetros da função adivinhe()
      if (palpite >= a & palpite <= b){
        
        # Caso o número fornecido pelo jogador seja igual ao escolhido pela
        # máquina, então mostramos a mensagem "Acertou" e encerramos a estrutura
        # de repetição repeat com o break
        if (palpite == sorteado) {
          cat("Acertou.")
          break
          
          # Caso o número seja menor que o escolhido pela máquina, mostramos
          # a mensagem "Tente um número maior"
        } else if (palpite < sorteado) {
          cat("Tente um número maior.")
          
          # Caso ele seja maior, mostramos a mensagem "Tente um número menor"
        } else {
          cat("Tente um número menor.")
        }
      }
      
      # Se o número escolhido estiver fora dos limites estabelecidos pelo usuário,
      # então mostramos a mensagem "Seu palpite está fora do intervalo"
      else{
        cat("Seu palpite está fora do intervalo.")
      }
    }
  }
}

# Instanciação da função adivinhe(), fornecendo (1,2) como argumentos para os parâmetros estabelecidos
# na declaração da função
adivinhe(1,10)
