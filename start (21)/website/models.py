from flaskapp import db

class User(db.Model):
    tablename = "user"
    user_id = db.Column(db.Integer, primary_key=True) 
    login = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    user_sname = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

def repr(self) -> str:
    return f"User(user_id {self.user_id!r}, name={self.user_fname!r}, surname={self.user_fname!r})"


class Jokes(db.Model):
    tablename = "joke"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    joke = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    

def repr(self) -> str:
    return f"Joke(id {self.id!r}, title ={self.title!r}, author ={self.author!r}, joke ={self.joke!r}, img_url ={self.img_url!r})"