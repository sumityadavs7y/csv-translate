import json
import string
import random
import os

import pandas as pd
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

from models.farmer import FarmerModel

LANGUAGE_CODES = ['en', 'mr', 'hi', 'te', 'pa']


def translate_and_save(file_path):
    df = pd.read_csv(file_path)
    credentials_json = json.loads(os.environ.get('GOOGLE_API_CREDENTIAL'))
    credentials = service_account.Credentials.from_service_account_info(
        credentials_json)
    translate_client = translate.Client(credentials=credentials)
    farmers = []
    for i in df.itertuples():
        unique_id = ''.join(random.choice(string.ascii_letters)
                            for i in range(6))
        for lc in LANGUAGE_CODES:
            cols = list(df.columns)
            reg_dict = translate_client.translate(cols, target_language=lc)
            reg_cols = [a['translatedText'] for a in reg_dict]
            reg_cols.insert(0, 'index')
            for idx, val in enumerate(i):
                if reg_cols[idx] != 'index':
                    if type(val) == str:
                        cell_reg_dict = translate_client.translate(
                            val, target_language=lc)
                        farmers.append(
                            FarmerModel(unique_id, lc, reg_cols[idx], cell_reg_dict['translatedText']))
                    else:
                        print(unique_id, reg_cols[idx], val)
                        farmers.append(
                            FarmerModel(unique_id, lc, reg_cols[idx], val))
    FarmerModel.commit_all(farmers)
    return True
