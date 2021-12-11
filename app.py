from flask import Flask
from flask_restful import Api

from resources.home import Home
from resources.farmer import UploadCSV


app = Flask(__name__)
api = Api(app)
api.add_resource(Home, '/')
api.add_resource(UploadCSV, '/upload')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
