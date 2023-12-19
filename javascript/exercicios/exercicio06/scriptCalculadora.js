$(document).ready(function() {
    const main = document.getElementsByTagName("main");
    let armazenador = "";
    let resultado = "";

    let novaCelulaResultado = $("<div>").text("");
    $("main").append(novaCelulaResultado);

    $("div").click(function(e) {
        if ($(this).text() !== "=" && $(this).text() !== "AC") {
            armazenador += "" + $(this).text();
            novaCelulaResultado.text(armazenador);

        } else {
            if ($(this).text() === "AC") {
                armazenador = "";
                novaCelulaResultado.text("");
            } else {
                resultado = eval(armazenador);
                armazenador = "";
                novaCelulaResultado.text(resultado);
            }
        }
    });
});
