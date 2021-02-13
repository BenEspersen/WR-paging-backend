from gevent.pywsgi import WSGIServer


class FlaskAppWrapper(object):

    def __init__(self, app):
        self.app = app

    def run(self):
        http_server = WSGIServer(('', 5000), self.app)
        print("Started Flask Server...")
        http_server.serve_forever()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods)
