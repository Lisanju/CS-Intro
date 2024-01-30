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

O formato mais comum de armazenar dados é o retangular, isto é, um dataframe com observações ao longo das linhas e variáveis ao longo das colunas.

Os valores de cada linha são separados por um caractere separador: vírgula, espaço, tab e etc.

As linhas são separadas por quebras de linha (`\r\n` no Windows).

As funções de importação de dados possuem um argumento relacionado a codificação (encoding) dos caracteres. Arquivos texto em português geralmente usam a codificação ISO 8859-1 ou equivalente Latin1.

O R usa o esquema de codificação UTF-8 para a associação unívoca de cada caractere a uma sequência de bits.

A especificação da codificação pode ser feita através do menu `Tools > Global Options > Code > Saving > Default Text Encoding`.

A biblioteca rio possui apoio para diversos formatos frequentemente usados. Para usar o rio, basicamente é necessário conhecer duas funções, que são `import` e `export`.

Os formatos suportados pelo rio são:

- .csv - Valores separados por vírgula;
- .tsv - Dados separados por tab;
- .xls / .xlsx - Excel;
- .RData / .rda - Objetos salvos no R;
- .rds - Objetos do R serializados;
- *sem extensão reconhecida - Dados Fortran;
- .fwf - Formato de dados com largura fixa;
- .feather - Feather R/Python interchange format;
- .fst - Armazenamento Rápido (Fast Storage);
- .json - JSON;
- .mat - Matlab;
- .ods - Planilha OpenDocument;
- .html - Tabelas HTML;
- .xml - Documentos XML.
