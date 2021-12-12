import os

from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from db import db
from resources.home import Home
from resources.farmer import UploadCSV, Farmers, Farmer

load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config['GOOGLE_API_CREDENTIAL'] = os.environ.get('GOOGLE_API_CREDENTIAL')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Home, '/')
api.add_resource(UploadCSV, '/upload')
api.add_resource(Farmers, '/farmers')
api.add_resource(Farmer, '/farmer/<farmer_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
