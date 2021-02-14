from flask import Flask
from FlaskWrapper import FlaskAppWrapper
from controller import DefaultController, loginController, createUserController, editUserController, addTaskController
from controller import acceptTaskController, listAllTasksForTechnikerController, closeTaskController
from controller import getOnlineTechnikerController, getTechnikerWithoutTaskController
from controller import fastpagingController, logoutController, addAusbildungToTechniker

if __name__ == '__main__':
    app = FlaskAppWrapper(Flask(__name__))

    app.add_endpoint(endpoint="/", endpoint_name="/", handler=DefaultController.handler, methods=['GET'])
    app.add_endpoint(endpoint="/login", endpoint_name="/login", handler=loginController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/createUser", endpoint_name="/createUser", handler=createUserController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/editUser", endpoint_name="/editUser", handler=editUserController.handler, methods=['PATCH'])
    app.add_endpoint(endpoint="/addTask", endpoint_name="/addTask", handler=addTaskController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/acceptTask", endpoint_name="/acceptTask", handler=acceptTaskController.handler, methods=['PATCH'])
    app.add_endpoint(endpoint="/listAllTasksForTechniker", endpoint_name="/listAllTasksForTechniker",
                     handler=listAllTasksForTechnikerController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/closeTask", endpoint_name="/closeTask", handler=closeTaskController.handler, methods=['DELETE'])
    app.add_endpoint(endpoint="/getOnlineTechniker", endpoint_name="/getOnlineTechniker", handler=getOnlineTechnikerController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/getOnlineTechnikerWithoutTask", endpoint_name="/getOnlineTechnikerWithoutTask",
                     handler=getTechnikerWithoutTaskController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/fastpageing", endpoint_name="/fastpaging", handler=fastpagingController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/logout", endpoint_name="/logout", handler=logoutController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/addAusbildungToTechniker", endpoint_name="/addAusbildungToTechniker", handler=addAusbildungToTechniker.handler, methods=['PATCH'])


    app.run()
