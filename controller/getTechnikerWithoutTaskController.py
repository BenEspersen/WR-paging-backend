from flask import request
from database.DatabaseService import DatabaseService


def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    if dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner")):
        techniker = dbService.getOnlineTechnikerWithoutTask()
        dbService.drop()
        return {"status": "successful", "techniker": techniker}
    else:
        dbService.drop()
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequest(data):
    return data.get("access_token") is not None and data.get("token_owner") is not None