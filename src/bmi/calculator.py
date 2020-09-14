from http import HTTPStatus

from aws_lambda_decorators import (cors, log, response_body_as_json, extract_from_event, Parameter, Mandatory, Minimum,
                                   Type, handle_exceptions, ExceptionHandler)
from src.logger import get_logger


LOGGER = get_logger(__name__)


GENERIC_ERROR = "Internal error"


@cors()
@log(parameters=True, response=True)
@handle_exceptions(handlers=[
    ExceptionHandler(Exception, GENERIC_ERROR, HTTPStatus.INTERNAL_SERVER_ERROR)
])
@response_body_as_json
@extract_from_event(parameters=[
    Parameter(path="/queryStringParameters/height", validators=[Mandatory, Type(int), Minimum(1)], transform=int),
    Parameter(path="/queryStringParameters/weight", validators=[Mandatory, Type(int), Minimum(1)], transform=int)
])
def handler(event: dict, context: dict, height: int = None, weight: int = None):  # pylint:disable=unused-argument
    LOGGER.info("Some info message")
    return {
        "statusCode": 200,
        "body": {
            "bmi": round(weight / (height / 100)**2, 2)
        }
    }
