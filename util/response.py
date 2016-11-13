# -*- coding: utf-8 -*-
import json

from flask import Response


class ResponseUtil:
    def __init__(self):
        pass

    @staticmethod
    def create_response(status=500, body='Please ask Administrator.', header=None):
        response_body = {'status': status, 'response': body}
        response_header = header if header is not None else {'Content-Type': 'application/json;charset=utf-8'}

        return Response(json.dumps(response_body), status, response_header)
