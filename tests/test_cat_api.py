# import pytest
import random
import unittest
from utils.cat_api import CatAPI


class TestCatAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cat_api_client = CatAPI()

    def setUp(self):
        self.get_votes_response = self.cat_api_client.get_votes()
        self.random_vote_id = random.choice(self.get_votes_response.json())['id']
        self.get_vote_response = self.cat_api_client.get_vote(self.random_vote_id)
        self.post_vote_response = self.cat_api_client.post_vote()
        self.json_post_vote_response = self.post_vote_response.json()
        self.post_vote_response_id = self.json_post_vote_response['id']

    def test_cat_api_1(self):
        self.assertEqual(self.get_votes_response.status_code, 200, '')

    def test_cat_api_2(self):
        self.assertGreater(len(self.get_votes_response.content), 0, '')

    def test_cat_api_3(self):
        self.assertEqual(self.get_vote_response.status_code, 200, '')

    def test_cat_api_4(self):
        self.assertGreater(len(self.get_vote_response.text), 0, '')

    def test_cat_api_5(self):
        self.assertEqual(self.post_vote_response.status_code, 201, '')

    def test_cat_api_6(self):
        self.assertNotEqual(self.post_vote_response_id, 0, '')

    def test_cat_api_7(self):
        self.assertEqual(self.json_post_vote_response['message'], 'SUCCESS', '')
