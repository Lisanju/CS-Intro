$(document).ready(function(){
    const button = $("#enviarCep");

    button.on("click", function(e){
        let cep = document.getElementById("digitarCep").value;
        getAndInsertCepInfo(cep);
    });

    function insert(data){
        $("#infoCorreios").append(
        "<tr>" +
            "<td>" + data.cep + "</td>" +
            "<td>" + data.logradouro + "</td>" +
            "<td>" + data.bairro + "</td>" +
            "<td>" + data.localidade + "</td>" +
            "<td>" + data.uf + "</td>" +
            "<td>" + data.ibge + "</td>" +
            "<td>" + data.gia + "</td>" +
            "<td>" + data.ddd + "</td>" +
        "</tr>");
    };

    function getAndInsertCepInfo(cep) {
        if (cep.length === 8){
            $.getJSON("https://viacep.com.br/ws/" + cep + "/json/", function(data) {
                $("#infoCorreios").empty();
                insert(data);
            });
        } else {
            window.alert("CEP inválido. Digite um CEP de 8 dígitos, sem traços ou pontos.")
        }
    }
});
