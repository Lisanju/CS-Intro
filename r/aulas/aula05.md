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
```

