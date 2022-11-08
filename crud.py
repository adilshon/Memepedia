from website.models import User,db

def add_user(user:User)->None:
    db.session.add(user)
    db.session.commit()

def delete_user(user:User)->None:
    db.session.delete(user)
    db.session.commit()

def get_all_user()->db.Query:
    return User.query.all()

