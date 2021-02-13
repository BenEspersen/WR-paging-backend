from flask import request
from database.DatabaseService import DatabaseService
from utils.JSON import Encoder


def handler():
    data = request.json
    if not checkRequest(data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    if dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner")):
        technikerID = dbService.FetchTechniker(data.get("token_owner")).ID
        aufgaben = dbService.listAllAuftraegeForTechniker(technikerID)
        dbService.drop()
        encoded = []
        for aufgabe in aufgaben:
            encoded.append(Encoder().encode(o=aufgabe))
        return {"status": "successful", "aufgaben": encoded}
    else:
        dbService.drop()
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequest(data):
    if data is not None:
        return data.get("access_token") is not None and data.get("token_owner") is not None
    else:
        return False
