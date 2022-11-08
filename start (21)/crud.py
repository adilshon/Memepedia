from website.models import User, db, Jokes

def add_user(user:User)->None:
    db.session.add(user)
    db.session.commit()

def delete_user(user:User)->None:
    db.session.delete(user)
    db.session.commit()

def get_all_user()->db.Query:
    return User.query.all()


def add_joke(joke:Jokes)->None:
    db.session.add(joke)
    db.session.commit()


def delete_joke(joke:Jokes)->None:
    db.session.delete(joke)
    db.session.commit()

def get_all_jokes()->db.Query:
    return Jokes.query.all()