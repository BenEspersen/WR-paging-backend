from flask import request
from database.DatabaseService import DatabaseService

def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    tokenStatus = dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner"))
    if tokenStatus:
        dbService.InsertTechniker(data.get("user_info"))
        dbService.drop()
        return {"status": "successful", "message": "successfully inserted techniker"}
    else:
        dbService.drop()
        return {"status": "failed", "message": "login credentials wrong"}

def checkRequest(data):
    if data is not None:
        if data.get("access_token") is not None and data.get("user_info") is not None and \
                data.get("token_owner") is not None:
            user_info = data.get("user_info")
            return user_info.get("name") is not None and \
                   user_info.get("vorname") is not None and \
                   user_info.get("klasse") is not None and \
                   user_info.get("schluessel") is not None and \
                   user_info.get("ausbildungen") is not None and \
                   user_info.get("aufgaben") is not None and \
                   user_info.get("password") is not None
        else:
            return False
    else:
        return False
