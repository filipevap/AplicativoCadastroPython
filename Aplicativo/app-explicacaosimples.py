from flask import Flask, render_template

app = Flask(__name__) #isso é padrão, não tem o que entender nem o que mudar
@app.route("/")  #aqui vai o caminho da página. se colocar apenas a "barra" ele direciona para a página home.
def homepage(): #aqui estou eu vou criar a função da homepage, que vai executar quando o caminho acima (que escolhemos a homepage) for acessado
    return "Meu site no Flask" #nesta função simples, ele irá apenas imprimir a string escrita

if __name__ == "__main__":
    app.run()




from flask import ( #aqui pesso para importar da biblioteca flask:
    Flask,          #a classe que cria o aplicativo web
    render_template,#Serve para carregar um arquivo HTML (o index.html.)
    jsonify,        #Transforma uma resposta Python em formato JSON, para que o navegador consiga entender.
    request,        #Permite receber dados enviados pelo usuário para o servidor.
)
import random n
app = Flask(__name__)   # isso é padrão, não tem o que entender nem o que mudar.
                        # É regra que está na documentação do Flask
                        # ele chama o site de app

#criar a 1ª página do app (do site)
    #Toda página tem o route (rota, endereço)
    
    #Toda página tem que ter uma função



@app.route("/")  #aqui vai o caminho da página. se colocar apenas a "barra" ele direciona para a página home.
def homepage(): #aqui estou eu vou criar a função da homepage, que vai executar quando o caminho acima (que escolhemos a homepage) for acessado
    return "Meu site no Flask" #nesta função simples, ele irá apenas imprimir a string escrita

if __name__ == "__main__":
#colocar o site no ar:
    app.run()
