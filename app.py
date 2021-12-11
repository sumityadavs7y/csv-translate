from flask import Flask
from flask_restful import Api

from resources.home import Home


app = Flask(__name__)
api = Api(app)
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
