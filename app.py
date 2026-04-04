from flask import Flask, render_template

app = Flask(__name__)

# Lista de produtos com os nomes das suas fotos na pasta static
produtos = [
    {
        "nome": "Meia Panturrilha Hobby",
        "preco": "59,90",
        "imagem": "static/Performance 1.jpg",
        "descricao": "Conforto e qualidade para o dia a dia."
    },
    {
        "nome": "Meia Sigvaris Dynaven",
        "preco": "149,90",
        "imagem": "static/Sigvaris Dynaven Basic Meia de Compressão 20-30.jpg",
        "descricao": "Alta tecnologia em compressão graduada."
    }
]

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)