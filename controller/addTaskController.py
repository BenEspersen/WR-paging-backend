from flask import request
from database.DatabaseService import DatabaseService
from utils.TechnikerSelector import TechnikerSelector

def handler():
    data = request.json
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    tokenStatus = dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner"))
    if tokenStatus:
        selector = TechnikerSelector(dbService)
        technikerID = selector.getTechniker(data.get("aufgabe"))
        if technikerID is None:
            dbService.drop()
            return {"status": "warning", "message": "Aktuell ist leider kein freier Techniker verfügbar"}
        dbService.addTask(data.get("name"), data.get("aufgabe"), technikerID, data.get("date"), data.get("treffpunkt"))
        dbService.drop()
        return {"status": "successful", "message": "successfully created Task for techniker"}
    else:
        dbService.drop()
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequest(data):
    if data is not None:
        return data.get("access_token") is not None and data.get("token_owner") is not None and \
               data.get("name") is not None and data.get("aufgabe")




