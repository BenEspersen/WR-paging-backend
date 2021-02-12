from flask import request
from database.DatabaseService import DatabaseService

def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    if data.get("category") == "id":
        return {"status": "failed", "message": "cannot update id. Blocked by service policy"}
    dbService = DatabaseService()
    tokenStatus = dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner"))
    if tokenStatus:
        dbService.UpdateTechniker(data.get("user"), data.get("category"), data.get("value"))
        dbService.drop()
        return {"status": "successful", "message": "successfully updated user " + data.get("user")}
    else:
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequest(data):
    return data.get("access_token") is not None and data.get("token_owner") is not None and \
        data.get("user") is not None and data.get("category") is not None and data.get("value") is not None