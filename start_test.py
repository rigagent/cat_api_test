import random
import unittest
from utils.cat_api import CatAPI


class CatAPITest(unittest.TestCase):

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

    def test_one(self):
        self.assertEqual(self.get_votes_response.status_code, 200, '')

    def test_two(self):
        self.assertGreater(len(self.get_votes_response.content), 0, '')

    def test_three(self):
        self.assertEqual(self.get_vote_response.status_code, 200, '')

    def test_four(self):
        self.assertGreater(len(self.get_vote_response.text), 0, '')

    def test_five(self):
        self.assertEqual(self.post_vote_response.status_code, 200, '')

    def test_six(self):
        self.assertNotEqual(self.post_vote_response_id, 0, '')

    def test_seven(self):
        self.assertEqual(self.json_post_vote_response['message'], 'SUCCESS', '')


if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(CatAPITest)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
