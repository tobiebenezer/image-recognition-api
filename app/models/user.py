from app.extension import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(225))
    email = db.Coumn(db.string(225))

    def __repr__(self):
        return f'<User "{self.name}" {self.email}>'