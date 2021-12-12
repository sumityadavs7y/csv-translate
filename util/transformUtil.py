import pandas as pd


def combine_key_and_value(ap):
    temp = {}
    for idx, a in ap.iterrows():
        temp[a['field_key']] = a['field_value']
    return temp


def combine_farmers(ap):
    temp = {}
    for idx, a in ap.iterrows():
        temp[a['language_code']] = a['data']
    return temp


def combine_all_farmers(farmers):
    df = pd.DataFrame.from_dict(farmers)
    k = df.groupby(['farmer_id', 'language_code']).apply(
        lambda x: pd.Series({'data': combine_key_and_value(x)})).reset_index()
    l = k.groupby(['farmer_id']).apply(
        lambda x: pd.Series({'data': combine_farmers(x)})).reset_index()
    temp = {}
    for idx, a in l.iterrows():
        temp[a['farmer_id']] = a['data']
    return temp
