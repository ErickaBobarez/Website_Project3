from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def stateofmatter():
    return render_template("StateofMatter.html")


@app.route("/gas")
def gas():
    return render_template("Gas.html")


@app.route("/liquid")
def liquid():
    return render_template("Liquid.html")


@app.route("/solid")
def solid():
    return render_template("Solid.html")


@app.route("/plasma")
def plasma():
    return render_template("Plasma.html")


if __name__ == "__main__":
    app.run()
