from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "hello"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/haha')
def haha():
    return "haha"


@app.route('/hihi')
def hihi():
    return render_template("hihi.html")


app.run(port=5002, host="0.0.0.0")
