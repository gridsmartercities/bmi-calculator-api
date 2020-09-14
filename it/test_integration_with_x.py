import unittest
from src.bmi.calculator import handler


class IntegrationTests(unittest.TestCase):

    def test_success(self):
        # ...

        response = handler(None, None)
        self.assertEqual(200, response["statusCode"])
        self.assertEqual("""{"message": "HELLO FROM A_LAMBDA"}""", response["body"])

        # ...
