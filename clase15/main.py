from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def index():
    #return "Hello, SmartNinja!"
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/porfolio")
def portfolio():
    return render_template("portfolio/index.html")

if __name__ == '__main__':
    app.run()