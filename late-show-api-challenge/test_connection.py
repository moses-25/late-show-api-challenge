from server.app import create_app
from server.models import db

app = create_app()

with app.app_context():
    try:
        db.session.execute("SELECT 1")
        print("✅ Database connection successful.")
    except Exception as e:
        print("❌ Database connection failed:", e)
