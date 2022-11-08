from flaskapp import *
from flask import render_template,request, session, redirect, url_for
from website.models import User
import crud


@app.route("/index")
@app.route("/")
def home():
    if session.get("authenticated"):
        user = db.session.query(User).filter_by(user_id=session['uid']).first()
        return render_template("index.html", context=user)
    return render_template("index.html")


@app.route('/profile/', methods=["GET"])
def user_page(context=None):
    query = db.session.query(User).filter(User.user_id == session.get("uid")).first()
    return render_template("user_page.html", context=query)




@app.route("/login", methods = ["GET", "POST"])
def login(context=None):
    if request.method == "POST":
        user = db.session.query(User).filter_by(login=request.form['username'], password=request.form['password']).first()
        print(user)
        if user:
            session['authenticated'] = True
            session['uid'] = user.user_id
            session['username'] = user.login
            return redirect(url_for("home"))
        else:
            return render_template("login.html", context="The login or username were wrong")

    return render_template("login.html", context=context)


@app.route("/logout")
def logout():
    session.pop('authenticated', None)
    session.pop('uid', None)
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/signup', methods = ["GET", "POST"])
def register(context=None):
    if request.method == "POST":
        login = request.form['username']
        fname = request.form['fname']
        sname = request.form['sname']
        pass1 = request.form['password']
        pass2 = request.form['password_conf']
    
        data = db.session.query(User).filter_by(login=request.form['username']).first()
        
        if data:
            return redirect(url_for("register", error="Already registered!"))
        elif pass1!=pass2:
            return redirect(url_for("register", error="Passwords do not match!"))
        else:
            crud.add_user(User(login=login, 
                                user_fname=fname,
                                user_sname=sname,
                                password=pass1))

            return redirect(url_for("login", context="Successfully registered!"))
    return render_template("signup.html", context=context)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
