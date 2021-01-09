from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String, index=True, default=datetime.utcnow)
    email = db.Column(db.String(120))
    name = db.Column(db.String(128))
    city = db.Column(db.String(128))
    contact = db.Column(db.String(128))
    age = db.Column(db.String(128))
    recent_company = db.Column(db.String(128))
    role_in_company = db.Column(db.String(128))
    current_ctc = db.Column(db.String(128))
    fixed_component_ctc = db.Column(db.String(128))
    experience = db.Column(db.String(128))
    comfort = db.Column(db.String(128))
    relocate = db.Column(db.String(128))
    rate_english = db.Column(db.String(128))
    skills = db.Column(db.String(128))
    industries = db.Column(db.String(128))
    profile = db.Column(db.String(128))
    factors = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.timestamp)  