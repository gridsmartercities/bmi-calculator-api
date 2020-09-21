import unittest
from unittest.mock import patch
from src.weight.weight_calculator import handler


class CalculatorTests(unittest.TestCase):

    @patch("src.weight.weight_calculator.LOGGER")
    def test_success(self, mock_logger):
        event = {
            "queryStringParameters": {
                "height": 180
            }
        }
        response = handler(event, None)
        self.assertEqual(200, response["statusCode"])
        self.assertEqual("""{"weight": 80}""", response["body"])
        mock_logger.info.assert_called_once_with("Some info message")
