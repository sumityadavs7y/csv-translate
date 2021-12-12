import os

from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from resources.home import Home
from resources.farmer import UploadCSV

load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config['GOOGLE_API_CREDENTIAL'] = os.environ.get('GOOGLE_API_CREDENTIAL')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(Home, '/')
api.add_resource(UploadCSV, '/upload')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
