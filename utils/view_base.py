import json
from flask import Response


def make_response(status_code=200, code=0, message='', body=None, mime_type="application/json"):
    result = {
        "code": code,
        "message": message,
        "body": body
    }
    response = Response(json.dumps(result), mimetype=mime_type)
    response.status_code = status_code
    return response
