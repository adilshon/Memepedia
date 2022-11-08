from flaskapp import db

class User(db.Model):
    tablename = "user"
    user_id = db.Column(db.Integer, primary_key=True) 
    login = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    user_sname = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    
def repr(self) -> str:
    return f"User(user_id {self.user_id!r}, name={self.user_fname!r}, surname={self.user_fname!r})"