Do not forget to first make and activate a virtual environment (e.g. ``python -m venv myvenv``, ``myvenv\Scripts\activate``) and then install some essential packages: ``pip install flask flask-wtf flask-sqlalchemy flask-login``.

Then run make_db **once** to create and seed the DB: ``python make_db.py``

Finally, run the app: ``python app.py``