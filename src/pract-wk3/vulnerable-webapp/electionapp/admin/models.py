from electionapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    polpref = db.Column(db.String(128), nullable=True)

    def __init__(self, username, password, polpref):
        self.username = username
        self.password = password
        self.polpref = polpref

    def check_password(self, password):
        return self.password == password