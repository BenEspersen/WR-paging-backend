from FlaskWrapper import FlaskAppWrapper
from controller import DefaultController, loginController, createUserController, editUserController, addTaskController
from controller import acceptTaskController, listAllTasksForTechnikerController, closeTaskController

if __name__ == '__main__':
    app = FlaskAppWrapper()

    app.add_endpoint(endpoint="/", endpoint_name="/", handler=DefaultController.handler, methods=['GET'])
    app.add_endpoint(endpoint="/login", endpoint_name="/login", handler=loginController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/createUser", endpoint_name="/createUser", handler=createUserController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/editUser", endpoint_name="/editUser", handler=editUserController.handler, methods=['PATCH'])
    app.add_endpoint(endpoint="/addTask", endpoint_name="/addTask", handler=addTaskController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/acceptTask", endpoint_name="/acceptTask", handler=acceptTaskController.handler, methods=['PATCH'])
    app.add_endpoint(endpoint="/listAllTasksForTechniker", endpoint_name="/listAllTasksForTechniker",
                     handler=listAllTasksForTechnikerController.handler, methods=['POST'])
    app.add_endpoint(endpoint="/closeTask", endpoint_name="/closeTask", handler=closeTaskController.handler, methods=['DELETE'])

    app.run()
