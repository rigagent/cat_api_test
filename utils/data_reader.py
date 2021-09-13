import json


DATA_FILE = 'config/data.json'


def read_data():
    with open(DATA_FILE, 'r') as f:
        json_data = json.load(f)
    return json_data


class DataReader:

    def __init__(self):
        test_data = read_data()
        self.protocol = test_data['protocol']
        self.host = test_data['host']
        self.api_version = test_data['api_version']
        self.auth_name = test_data['auth_name']
        self.auth_value = test_data['auth_value']
