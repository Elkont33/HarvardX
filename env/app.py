from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("hello.html")
@app.route("/<string:name>")
def hello(name):
    return f"Hello {name}!"