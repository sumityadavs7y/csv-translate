import os

from flask_restful import Resource, request
from werkzeug.utils import secure_filename

from models.farmer import FarmerModel
from util.transformUtil import combine_all_farmers
from util.translateUtil import translate_and_save

ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadCSV(Resource):
    def post(self):
        if 'file' not in request.files:
            return {'message': 'no file found.'}, 404
        file = request.files['file']

        if file.filename == '':
            return {'message': 'no file selected.'}, 404

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(os.curdir, 'uploads', filename)
            try:
                file.save(file_path)
            except Exception as e:
                return {'message': 'not able to save file.'}, 500
            if translate_and_save(file_path):
                return {'message': 'file saved.'}, 201
            else:
                return {'message': 'error in translating'}, 500
        else:
            return {'message': 'file not found ot not allowed.'}, 400


class Farmers(Resource):
    def get(self):
        farmers = [farmer.json() for farmer in FarmerModel.find_all()]
        if len(farmers) == 0:
            return {"message": "no farmer found"}, 404
        ret_val = combine_all_farmers(farmers)
        return {"farmers": ret_val}, 200


class Farmer(Resource):
    def get(self, farmer_id):
        farmers = [farmer.json()
                   for farmer in FarmerModel.find_by_farmer_id(farmer_id)]
        if len(farmers) == 0:
            return {"message": "no farmer found"}, 404
        ret_val = combine_all_farmers(farmers)
        return ret_val, 200
