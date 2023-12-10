# Sintaxe básica em HTML

O HyperText Markup Language (HTML) é uma linguagem de marcação, que possui rótulos de marcação que definem as páginas Web.

As Tags HTML (rótulos de marcação) são palavras-chaves envolvidas por < > que normalmente aparecem em dupla: as tags de abertura e as de fechamento. As Web Pages (Documentos HTML) são conjuntos de Tags HTML em arquivos de texto pleno.

Por exemplo:
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Estrutura básica de um arquivo HTML</title>
    </head>
    <body>
        <h1> Esta tag serve para denotar um Título-1 </h1>
        <p> Esta tag serve para denotar um Parágrafo-1 </p>
    </body>
</html>
```

- A declaração `<!DOCTYPE html>` define este documento como sendo HTML5.
- O elemento `<head>` contém os metadados do documento HTML. Metadados são dados que definem outros dados, ou seja, descrevem características do documento, normalmente definindo o título do documento, sua codificação, estilos e scripts.
- O texto entre `<html>` e `</html>` descreve a página Web.
- O texto entre `<body>` e `</body>` é a parte visível do conteúdo da página.
- O texto entre `<h1>` e `</h1>` é mostrado como um título.
- O texto entre `<p>` e `</p>` é mostrado como um parágrafo.
