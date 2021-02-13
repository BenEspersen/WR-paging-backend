from flask import request
from database.DatabaseService import DatabaseService


def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    if dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner")):
        dbService.acceptTask(data.get("auftragsID"))
        dbService.updateTechnikerTask(data.get("auftragsID"), data.get("token_owner"))
        dbService.drop()
        return {"status": "successful", "message": "successfully accepted task"}
    else:
        dbService.drop()
        return {"status": "error", "message": "your json request body is wrong"}


def checkRequest(data):
    if data is not None:
        return data.get("access_token") is not None and data.get("token_owner") is not None and \
            data.get("auftragsID") is not None
    else:
        return False
