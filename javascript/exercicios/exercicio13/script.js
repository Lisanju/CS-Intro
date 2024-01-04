$(document).ready(function() {
    const bPadrao = $(".bPadrao");

    const bCadastrar = $("#bCadastrar");

    const tTituloEsquerda = $("#tTituloEsquerda");
    const tPrecoEsquerda = $("#tPrecoEsquerda");
    const tDescricaoEsquerda = $("#tDescricaoEsquerda");

    function handleMouseEvents(element, color) {
        element.on("mouseover", function() {
            $(this).css({
                "border": "4px",
                "border-color": color,
                "border-style": "solid"
            });
        });

        element.on("mouseout", function() {
            $(this).css({
                "border": "4px",
                "border-color": "white",
                "border-style": "solid"
            });
        });
    }

    bCadastrar.on("click", function(e) {
        $.ajax({
            url: "https://banco-dados-teste.glitch.me/api/produtos",
            type: "POST",
            data: {
                title: tTituloEsquerda.val(),
                price: tPrecoEsquerda.val(),
                description: tDescricaoEsquerda.val(),
            },
            success: function(data) {
                alert("Produto cadastrado com sucesso!")

                tTituloEsquerda.val("");
                tPrecoEsquerda.val("");
                tDescricaoEsquerda.val("");

                $("tbody").append(`<tr>
                    <td>${data.title}</td>
                    <td>${data.price}</td>
                    <td><input type="button" class="bDeletar" data-id="${data._id}" value="Deletar">
                        <input type="button" class="bExibir" value="Exibir"></td>
                </tr>`);

                handleMouseEvents($(".bDeletar:last"), "indianred");
                handleMouseEvents($(".bExibir:last"), "lightgreen");
            },
        });
    });

    handleMouseEvents(bPadrao, "skyblue");
});
