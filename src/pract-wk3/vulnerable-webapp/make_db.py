from electionapp import db, app
from electionapp.voting.models import Party
from electionapp.admin.models import User

with app.app_context():
    db.create_all()
    db.session.add_all([Party('Piratenpartij'), Party('DOS 66'), Party('Volkspartij voor Vrijheid van Data')])
    db.session.add_all([User('admin', 'admin', 'rechts'), User('henk', '1234', 'links')])
    db.session.commit()