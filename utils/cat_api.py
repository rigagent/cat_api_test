import requests
from utils.data_reader import DataReader


class CatAPI:

    def __init__(self):
        self.data = DataReader()
        self.headers = {self.data.auth_name: self.data.auth_value}

    def get_votes(self):
        return requests.get(url=f'{self.data.protocol}://{self.data.host}/{self.data.api_version}/votes',
                            headers=self.headers)

    def get_vote(self, vote_id):
        return requests.get(url=f'{self.data.protocol}://{self.data.host}/{self.data.api_version}/votes/{vote_id}',
                            headers=self.headers)

    def post_vote(self):
        payload = {
            "image_id": "asf2",
            "sub_id": "my-user-1234",
            "value": 1
        }
        return requests.post(url=f'{self.data.protocol}://{self.data.host}/{self.data.api_version}/votes', json=payload,
                             headers=self.headers)

    def delete_vote(self, vote_id):
        return requests.delete(url=f'{self.data.protocol}://{self.data.host}/{self.data.api_version}/votes/{vote_id}',
                               headers=self.headers)
