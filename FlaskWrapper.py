from flask import Flask


class FlaskAppWrapper(object):

    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods)
