from flask import Flask

app = Flask(__name__)


@app.route("/prefeito")
def prefeito():
    return "<h1>DR Jarques!</h1>"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run(debug=True)
