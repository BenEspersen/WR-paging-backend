from FlaskWrapper import FlaskAppWrapper
from controller import DefaultController, loginController

if __name__ == '__main__':
    app = FlaskAppWrapper()

    app.add_endpoint(endpoint="/", endpoint_name="/", handler=DefaultController.handler, methods=['GET'])
    app.add_endpoint(endpoint="/login", endpoint_name="/login", handler=loginController.handler, methods=['POST'])

    app.run()
