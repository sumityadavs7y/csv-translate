from db import db


class Farmer(db.Model):
    __tablename__ = 'farmer'

    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.String(20), nullable=False)
    language_code = db.Column(db.String(256), nullable=False)
    field_key = db.Column(db.String(256), nullable=False)
    field_value = db.Column(db.String(256), nullable=False)

    def __init__(self, farmer_id, language_code, field_key, field_value):
        self.farmer_id = farmer_id
        self.language_code = language_code
        self.field_key = field_key
        self.field_value = field_value

    @classmethod
    def find_by_farmer_id(cls, farmer_id):
        return cls.quert.filter_by(farmer_id=farmer_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
