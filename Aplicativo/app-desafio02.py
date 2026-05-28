from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

lista = []


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    nome = dados["nome"].strip()
    idade = dados["idade"]
    curso = dados["curso"]

    if nome == "":
        return jsonify({"erro": "Digite o nome."}), 400

    try:
        idade = int(idade)
    except:
        return jsonify({"erro": "Digite uma idade valida."}), 400

    if idade <= 0:
        return jsonify({"erro": "A idade precisa ser maior que zero."}), 400

    if idade <= 12:
        tipo = "Crianca"
    elif idade <= 17:
        tipo = "Adolescente"
    else:
        tipo = "Adulto"

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "tipo": tipo,
    }

    lista.append(aluno)

    return jsonify({"lista": lista, "total": len(lista)})


@app.route("/limpar", methods=["POST"])
def limpar():
    lista.clear()
    return jsonify({"lista": lista, "total": len(lista)})


if __name__ == "__main__":
    app.run(debug=True)
