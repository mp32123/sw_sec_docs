from electionapp import db, app
from electionapp.voting.models import Party
from electionapp.admin.models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    db.session.add_all([Party('Piratenpartij'), Party('DOS 66'), Party('Volkspartij voor Vrijheid van Data')])
    db.session.add_all([User('admin', generate_password_hash('admin'), 'rechts'), User('henk', generate_password_hash('1234'), 'links')])

    db.session.commit()