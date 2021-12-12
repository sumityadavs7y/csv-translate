import os
from flask_restful import Resource, request
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def translate_and_save(file_path):
    return True


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
