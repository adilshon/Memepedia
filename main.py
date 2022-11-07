from flask import request, render_template, redirect, url_for, session, Flask


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login(context=None):
    return render_template("login.html", context=context)


@app.route('/profile', methods=["GET"])
def profile(context=None):
    return render_template("profile.html")


@app.route("/register", methods=["GET", "POST"])
def register(context=None):
    return render_template("register.html", context=context)


@app.route("/favorites", methods=["GET", "POST"])
def favorites(context=None):
    return render_template("favorites.html", context=context)



@app.route("/catalogue", methods=["GET", "POST"])
def catalogue(context=None):
    return render_template("catalogue.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)