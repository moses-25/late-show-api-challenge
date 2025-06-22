export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
