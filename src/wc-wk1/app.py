from mijnproject import app,db
from flask import render_template, redirect, request, url_for, flash, session
from flask_login import login_user, login_required, logout_user
from mijnproject.models import User
from mijnproject.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/welkom')
@login_required
def welkom():
    return render_template('welkom.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.check_password(form.password.data):
                login_user(user)
                session['role'] = 'user' # get from DB: user.role
                flash('Succesvol ingelogd.')
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('welkom')
                return redirect(next)
            else:
                flash('Inlog mislukt.')
        else:
            flash('Inlogformulier incorrect ingevuld.')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit() and form.check_email(form.email) and form.check_username(form.username):
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Dank voor de registratie. Er kan nu ingelogd worden!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/info')
@login_required
def info():
    if (session['role'] == 'admin'):
        return render_template('info.html')
    else:
        return render_template('not-allowed.html')

if __name__ == '__main__':
    app.run(debug=True)
