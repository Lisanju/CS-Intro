# Entrada e saída de dados

O R pode importar e exportar dados de diversas fontes, formatos e tamanhos. Muitas bibliotecas permitem lidar com essa diversidade de entrada e saída de dados.

Para reproduzir os códigos desta aula, serão necessárias as bibliotecas a seguir:

```
pacotes <- c(
  "easypackages",
  "rio",
  "readr",
  "feather",
  "readxl",
  "writexl",
  "dplyr",
  "microbenchmark",
  "openxlsx"
)

install.packages(pacotes)

library("easypackages")
library("rio")
library("readr")
library("writexl")
library("dplyr")
library("microbenchmark")
library("openxlsx")
```

Para carregar diversos pacotes de uma vez só, você pode usar a função `libraries` da biblioteca easypackages. Então o trecho de código anterior poderia ser substituído por:

```
library(easypackages)

libraries(pacotes)

# ou simplesmente

easypackages::libraries(pacotes)
```

## Diretório de trabalho

O R possui várias funções para obter informações do sistema, como arquivos e diretórios. É importante especificar o diretório de trabalho atual.

Importar ou exportar dados é mais fácil quando você não precisa digitar caminhos longos de diretórios para os arquivos. Por isso, quando abrimos uma sessão no R, ela é vinculada a um diretório de trabalho (working directory, wd). A função `getwd` retorna o diretório de trabalho da sua sessão do R.

```
getwd()
```

Para alterar seu wd, é possível usar a função `setwd()`.

```
wd <- getwd()

# define o wd em "/home/user"
setwd("~/Documents")
getwd()

# volta para o wd original
setwd(wd)
getwd()
```

## Arquivos texto

## Arquivos binários

## Arquivos Excel

