import os
import requests
import unittest


BASE_URL = os.environ.get("BASE_URL", None)
# BASE_URL = "https://mnqmg5khn4.execute-api.eu-west-2.amazonaws.com/Prod"


class ContractTests(unittest.TestCase):

    def test_success(self):
        response = requests.get(f"{BASE_URL}/bmi?height=179&weight=58")
        self.assertEqual(response.json(), {"bmi": 18.1})
