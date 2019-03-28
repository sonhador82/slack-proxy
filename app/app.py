#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask, request, logging, Response
from tasks import send

flask_app = Flask(__name__)

@flask_app.route('/post_event', methods=['POST'])
def post_event():
    send.delay(request.json)
    return Response("OK", 200, {'Content-Type': 'application/json'})


if __name__ == '__main__':
    flask_app.run(debug=True)
