from flask import request

from database.DatabaseService import DatabaseService


def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    if dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner")):
        dbService.addAusbildungToTechniker(data.get("username"), data.get("ausbildung"))
        dbService.drop()
        return {"status": "successful", "message": "successfully added ausbildung to techniker"}
    else:
        dbService.drop()
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequest(data):
    if data is not None:
        return data.get("access_token") is not None and data.get("token_owner") is not None and \
            data.get("username") is not None and data.get("ausbildung") is not None
