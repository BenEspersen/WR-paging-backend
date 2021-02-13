from flask import request

from database.DatabaseService import DatabaseService


def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    dbService.removeTokenFromDatabase(data.get("access_token"), data.get("token_owner"))
    dbService.drop()
    return {"status": "unknown", "message": "if there was a token, its deleted now :)"}


def checkRequest(data):
    if data is not None:
        return data.get("access_token") is not None and data.get("token_owner") is not None
    else:
        return False