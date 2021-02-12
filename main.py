from FlaskWrapper import FlaskAppWrapper
from controller import DefaultController
from utils.Encryption import EndToEndEncryption

if __name__ == '__main__':
    EndToEndEncryption()
    app = FlaskAppWrapper()

    app.add_endpoint(endpoint="/", endpoint_name="/", handler=DefaultController.handler, methods=['GET'])

    app.run()
