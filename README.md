# CSV Translator

## Question:
Your web application should be accessible through the following API endpoints -
1. An API which enables users to upload the farmer list via a csv file and translates thedata into supported languages. Sample list here. Download the sample list as a csv totest out your solution.
2. An API which allows us to retrieve all farmer data in the subset of languages specified above.

## Documentation

| Endpoint        | Method           | Input  |Input Example|Output  |Output Example|
| ------------- |:-------------:| -----:|-----:|-----:|-----:|
| `/upload`    | `POST` | `form-data: { "file":<any_csv_file: CSV file> }` |None|`{"message": <success/failure message>}`|`{"message":  "file saved."}`|
| `/farmers`      | `GET`      |   None |None|`{"farmers":{<farmer_id>:{<language_code>:{<farmer_detail_key>:<farmer_detail_value>}}}}`|`{"farmers":{"HiyaaB":{"en":{"phone_number":"666666666","farmer_name":"Aanandan","state_name":"Maharashtra","district_name":"Amravati","village_name":"Amravati"},"hi":{"फ़ोन नंबर":"666666666","किसान_नाम":"आनंदन","राज्य का नाम":"महाराष्ट्र","जिला_नाम":"अमरावती","गांव_नाम":"अमरावती"},"pa":{"ਫੋਨ ਨੰਬਰ":"666666666","ਕਿਸਾਨ_ਨਾਮ":"ਆਨੰਦਨ","ਰਾਜ_ਨਾਮ":"ਮਹਾਰਾਸ਼ਟਰ","ਜ਼ਿਲ੍ਹਾ_ਨਾਮ":"ਅਮਰਾਵਤੀ","ਪਿੰਡ_ਨਾਮ":"ਅਮਰਾਵਤੀ"}}}}`|
| `/farmer/<farmer_id>`      | `GET`      |   None |None|`{<farmer_id>:{<language_code>:{<farmer_detail_key>:<farmer_detail_value>}}}}`|`{"HiyaaB":{"en":{"phone_number":"666666666","farmer_name":"Aanandan","state_name":"Maharashtra","district_name":"Amravati","village_name":"Amravati"},"hi":{"फ़ोन नंबर":"666666666","किसान_नाम":"आनंदन","राज्य का नाम":"महाराष्ट्र","जिला_नाम":"अमरावती","गांव_नाम":"अमरावती"},"pa":{"ਫੋਨ ਨੰਬਰ":"666666666","ਕਿਸਾਨ_ਨਾਮ":"ਆਨੰਦਨ","ਰਾਜ_ਨਾਮ":"ਮਹਾਰਾਸ਼ਟਰ","ਜ਼ਿਲ੍ਹਾ_ਨਾਮ":"ਅਮਰਾਵਤੀ","ਪਿੰਡ_ਨਾਮ":"ਅਮਰਾਵਤੀ"}}`|


## Dependencies

##### Following are the external libraries used:
- flask
- flask-restful
- sqlalchemy
- flask-sqlalchemy
- python-dotenv
- google
- google-cloud-translate
- pandas

##### Following are the libraries used for dev environment:

- autopep8

for more details of the libraries Pipfile can be seen.

## Installation

CSV-Translate requires [python](https://www.python.org/) v3.8+ to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install pipenv
pipenv install
pipenv run python app.py
```

add your google translate api credentials in .env file. for example:
```
GOOGLE_API_CREDENTIAL = '{
    "type": "service_account",
    "project_id": "exaple-project-123",
    "private_key_id": "e6e5a29605ded8d2cf11a9c2a61314f93f9f01cb",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiertwertwetM6AtAKtnAB4vrCf/AjIh3U2VEqF1weryhdfgdsMbOY/S\no6a1vX+hIO+3eO6WPiDN1fbyhNjiSwdwCcDHJUZhmBTNZ9E7yJFN/Ft1N7yRh8sdfgsdfg96Hyf9B9nSOJG9mr7OKYaloVuicVOm\n3ES0MtN6+iM/+GyQPk0DPAwGesAwLxKAYskXEF9T18iOb2bV8f+9uHPM8fxhbb41\nlvW0TTfHj2p5q+IRHKwCIQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "example@example123.iam.gserviceaccount.com",
    "client_id": "123421223485723481",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/example%40project-123555.iam.gserviceaccount.com"
}'
```