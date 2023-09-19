from app.models.user import User
from app.extension import db


user = User(name="tobi samuel",
     email="tobi@mail.com")

db.session.add(post)
print(user)
print("--------")
db.session.commit()