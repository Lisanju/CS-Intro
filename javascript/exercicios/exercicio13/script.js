$(document).ready(function() {
	const bPadrao = $(".bPadrao");
	const bEditar = $("#bEditar");
	const bCadastrar = $("#bCadastrar");

	const tTituloEsquerda = $("#tTituloEsquerda");
	const tPrecoEsquerda = $("#tPrecoEsquerda");
	const tDescricaoEsquerda = $("#tDescricaoEsquerda");

	const tTituloDireita = $("#tTituloDireita");
	const tPrecoDireita = $("#tPrecoDireita");
	const tDescricaoDireita = $("#tDescricaoDireita");

	let produtoAtualmenteFocado;

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

				listarProdutos();
			},
		});
	});

	function listarProdutos() {
		$.ajax({
			url: "https://banco-dados-teste.glitch.me/api/produtos",
			type: "GET",
			success: function(data) {
				$("tbody").empty();

				data.forEach(function(produto) {
					$("tbody").append(`<tr>
                        <td>${produto.title}</td>
                        <td>${produto.price}</td>
                        <td>
                            <input type="button" class="bDeletar" data-id="${produto._id}" value="Deletar">
                            <input type="button" class="bExibir" data-id="${produto._id}" value="Exibir">
                        </td>
                    </tr>`);
				});

				handleMouseEvents($(".bDeletar"), "indianred");
				handleMouseEvents($(".bExibir"), "lightgreen");
			},
			error: function(error) {
				console.log("Erro ao listar produtos:", error);
			},
		});
	}

	listarProdutos();

	$("tbody").on("click", ".bDeletar", function() {
		const produtoId = $(this).data("id");

		$.ajax({
			url: `https://banco-dados-teste.glitch.me/api/produtos/${produtoId}`,
			type: "DELETE",
			success: function(data) {
				alert("Produto deletado com sucesso!");
				listarProdutos();
			},
			error: function(error) {
				console.log("Erro ao deletar produto:", error);
			},
		});
	});

	$("tbody").on("click", ".bExibir", function() {
		produtoAtualmenteFocado = $(this).data("id");
		const produtoId = produtoAtualmenteFocado;

		$("direita").css({
			"display": "flex"
		});

		$.ajax({
			url: `https://banco-dados-teste.glitch.me/api/produtos/${produtoId}`,
			type: "GET",
			success: function(data) {
				tTituloDireita.val(`${data.title}`);
				tPrecoDireita.val(`${data.price}`);
				tDescricaoDireita.val(`${data.description}`);
			},
		});
	});

	bEditar.on("click", function() {
		const produtoId = produtoAtualmenteFocado;

		$.ajax({
			url: `https://banco-dados-teste.glitch.me/api/produtos/${produtoId}`,
			type: "PUT",
			data: {
				title: tTituloDireita.val(),
				price: tPrecoDireita.val(),
				description: tDescricaoDireita.val(),
			},
			success: function(data) {
				alert("Produto editado com sucesso!");
				tTituloDireita.val("");
				tPrecoDireita.val("");
				tDescricaoDireita.val("");
				$("direita").css({
					"display": "none"
				});
				listarProdutos();
			},
			error: function(error) {
				console.log("Erro ao editar produto:", error);
			},
		});
	});

	handleMouseEvents(bPadrao, "skyblue");
});
