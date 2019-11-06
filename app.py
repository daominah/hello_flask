from flask import Flask, render_template, send_file

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


@app.route('/i1')
def handleI1():
    path = "images/i1.jpeg"
    return send_file(path, mimetype='image/jpeg')


app.run(port=5002, host="0.0.0.0")
