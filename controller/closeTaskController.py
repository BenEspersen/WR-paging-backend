from flask import request
from database.DatabaseService import DatabaseService

def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    if dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner")):
        auftragsID = dbService.getActiveTaskOfUser(data.get("token_owner"))
        dbService.finishTask(auftragsID)
        dbService.updateTechnikerTask('', data.get("token_owner"))
        dbService.drop()
        return {"status": "successful", "message": "successfully closed task"}
    else:
        dbService.drop()
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequest(data):
    return data.get("access_token") is not None and data.get("token_owner") is not None