from flaskapp import *
from flask import render_template,request, session, redirect, url_for
from website.models import User, Jokes
import crud
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


@app.route("/index")
@app.route("/")
def home():
    if session.get("authenticated"):
        user = db.session.query(User).filter_by(user_id=session['uid']).first()
        return render_template("index.html", context=user)
    return render_template("index.html")


@app.route('/profile/', methods=["GET"])
def user_page(context=None):
    user = db.session.query(User).filter(User.user_id == session.get("uid")).first()
    return render_template("user_page.html", context=user.as_dict())


@app.route("/catalogue")
def catalogue():
    return render_template("catalogue.html")


@app.route("/favorites")
def favorites():
    return render_template("favorites.html") #Here should be added user_id


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

@app.route('/upload', methods =["GET", "POST"])
def upload_meme(context=None):
    if request.method == "POST":
        f = request.files["file_to_save"]
        f.save(f"saved files/{secure_filename(f.filename)}")
        return redirect(url_for('upload_meme', context={"Status":"Successfully uploaded"}))
    return render_template("upload_meme.html", context=context)


@app.route('/upj', methods = ["GET", "POST"])
def upj():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        joke = request.form['joke']
        img_url = request.form['img_url']


        

        try:
            crud.add_joke(Jokes(title=title,
                                author=author,
                                joke=joke,
                                img_url=img_url))
            return redirect(url_for('home'))
        except:
            return "Mistake"
    else:
        return render_template("upload_joke.html")

@app.route('/jok')
def jok():
    jok = Jokes.query.order_by(Jokes.author).all()
    return render_template('show_joke.html', data=jok)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)