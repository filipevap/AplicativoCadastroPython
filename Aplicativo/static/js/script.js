function cadastrar() {
    var nome = document.getElementById("nome").value;
    var idade = document.getElementById("idade").value;
    var curso = document.getElementById("curso").value;

    fetch("/cadastrar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nome: nome,
            idade: idade,
            curso: curso
        })
    })
    .then(function(resposta) {
        return resposta.json().then(function(dados) {
            if (resposta.ok == false) {
                document.getElementById("mensagem").innerText = dados.erro;
            } else {
                document.getElementById("mensagem").innerText = "";
                mostrarLista(dados.lista);
                document.getElementById("total").innerText = dados.total;
                document.getElementById("nome").value = "";
                document.getElementById("idade").value = "";
            }
        });
    });
}

function limparLista() {
    fetch("/limpar", {
        method: "POST"
    })
    .then(function(resposta) {
        return resposta.json();
    })
    .then(function(dados) {
        mostrarLista(dados.lista);
        document.getElementById("total").innerText = dados.total;
        document.getElementById("mensagem").innerText = "";
    });
}

function mostrarLista(lista) {
    var divLista = document.getElementById("lista");
    divLista.innerHTML = "";

    for (var i = 0; i < lista.length; i++) {
        divLista.innerHTML += `
            <div class="card">
                <h3>${lista[i].nome}</h3>
                <p>Idade: ${lista[i].idade}</p>
                <p>Curso: ${lista[i].curso}</p>
                <p>Classificacao: ${lista[i].tipo}</p>
            </div>
        `;
    }
}
