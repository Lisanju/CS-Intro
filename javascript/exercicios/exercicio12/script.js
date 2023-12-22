$(document).ready(function(){
    $("#b").on("click", function(e){
        $.ajax({
            url: "texto.html",
            success: function(data){
                $("div").html(data);
            },
            beforeSend: function(){
                $("img").css({display:"block"});
            },
            complete: function(){
                $("img").css({display:"none"});
            }
        });
    });
});
