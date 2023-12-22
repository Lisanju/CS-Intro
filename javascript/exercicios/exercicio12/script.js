$(document).ready(function(){
    const bPadrao = $(".bPadrao");
    const bDeletar = $(".bDeletar");
    const bExibir = $(".bExibir");
    const bCadastrar = $("#bCadastrar");
    const bEditar = $("#bEditar");
    let sw = false;

    bPadrao.on("mouseover", function(e){
        $(this).css({"border":"4px","border-color":"skyblue","border-style":"solid"}); 
    });

    bPadrao.on("mouseout", function(e){
        $(this).css({"border":"4px","border-color":"white","border-style":"solid"}); 
    });

    bDeletar.on("mouseover", function(e){
        $(this).css({"border":"4px","border-color":"indianred","border-style":"solid"}); 
    });

    bDeletar.on("mouseout", function(e){
        $(this).css({"border":"4px","border-color":"white","border-style":"solid"}); 
    });

    bExibir.on("mouseover", function(e){
        $(this).css({"border":"4px","border-color":"lightgreen","border-style":"solid"}); 
    });

    bExibir.on("mouseout", function(e){
        $(this).css({"border":"4px","border-color":"white","border-style":"solid"}); 
    });

    bExibir.on("click", function(e){
        if (sw === false){
            $("direita").css({"display":"block"})
            sw = true;
            return sw;
        }
        $("direita").css({"display":"none"})
        sw = false;
        return sw;
    });
});
