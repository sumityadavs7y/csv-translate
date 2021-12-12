from db import db


class FarmerModel(db.Model):
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

    def json(self):
        return {
            "farmer_id": self.farmer_id,
            "language_code": self.language_code,
            "field_key": self.field_key,
            "field_value": self.field_value
        }

    @classmethod
    def find_by_farmer_id(cls, farmer_id):
        return cls.query.filter_by(farmer_id=farmer_id).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def commit_all(cls, farmers):
        for farmer in farmers:
            db.session.add(farmer)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
