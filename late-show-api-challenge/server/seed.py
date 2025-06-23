from server.models import db, User, Guest, Episode, Appearance
from server.app import app
from werkzeug.security import generate_password_hash

with app.app_context():
    print("🌱 Seeding data...")

    # Clear existing data (order matters due to FK relationships)
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    User.query.delete()

    # Create users
    user = User(username="admin", password_hash=generate_password_hash("admin123"))
    db.session.add(user)

    # Create guests
    guest1 = Guest(name="Moses Otieno", occupation="Software Engineer")
    guest2 = Guest(name="Patricia Mutongoi", occupation="Entrepreneur")

    # Create episodes
    episode1 = Episode(date="2025-04-01", number=1)
    episode2 = Episode(date="2025-04-02", number=2)

    # Add guests and episodes
    db.session.add_all([guest1, guest2, episode1, episode2])
    db.session.commit()

    # Create appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)

    db.session.add_all([appearance1, appearance2])
    db.session.commit()

    print("✅ Done seeding!")
