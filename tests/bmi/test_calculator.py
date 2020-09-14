import unittest
from unittest.mock import patch
from src.bmi.calculator import handler


class CalculatorTests(unittest.TestCase):

    @patch("src.bmi.calculator.LOGGER")
    def test_success(self, mock_logger):
        event = {
            "queryStringParameters": {
                "height": 180,
                "weight": 80
            }
        }
        response = handler(event, None)
        self.assertEqual(200, response["statusCode"])
        self.assertEqual("""{"bmi": 24.69}""", response["body"])
        mock_logger.info.assert_called_once_with("Some info message")
