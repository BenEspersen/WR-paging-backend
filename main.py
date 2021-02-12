from FlaskWrapper import FlaskAppWrapper
from controller import DefaultController

if __name__ == '__main__':
    app = FlaskAppWrapper()

    app.add_endpoint(endpoint="/", endpoint_name="/", handler=DefaultController.handler, methods=['GET'])

    app.run()
