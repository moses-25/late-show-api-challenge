from server.models import db

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    occupation = db.Column(db.String(120), nullable=False)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
        }
