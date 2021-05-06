import unittest
import json
from unittest.mock import patch
from src.height.height import handler


class CalculatorTests(unittest.TestCase):

    def test_success_height_below_average(self):
        event = {
            "queryStringParameters": {
                "height": 171
            }
        }

        expected_response = {
            "status": "Height is average",
        }

        response = handler(event, None)
        body = json.loads(response["body"])

        self.assertDictEqual(body, expected_response)
        self.assertEqual(200, response["statusCode"])

    def test_success_height_over_average(self):
        event = {
            "queryStringParameters": {
                "height": 160
            }
        }

        expected_response = {
            "status": "Height is below average",
        }

        response = handler(event, None)
        body = json.loads(response["body"])

        self.assertDictEqual(body, expected_response)
        self.assertEqual(200, response["statusCode"])

    def test_success_height_is_average(self):
        event = {
            "queryStringParameters": {
                "height": 180
            }
        }

        expected_response = {
            "status": "Height is over average",
        }

        response = handler(event, None)
        body = json.loads(response["body"])

        self.assertDictEqual(body, expected_response)
        self.assertEqual(200, response["statusCode"])

