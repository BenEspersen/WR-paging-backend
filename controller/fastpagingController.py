from flask import request

from database.DatabaseService import DatabaseService


def handler():
    data = request.json
    print(data)
    if not checkRequest(data=data):
        return {"status": "error", "message": "your json request body is wrong"}
    dbService = DatabaseService()
    tokenStatus = dbService.CheckPermissionViaToken(data.get("access_token"), data.get("token_owner"))
    if tokenStatus:
        if data.get("call_type") == "techniker":
            # send notification to user
            return {"status": "successful", "message": "send notification to user"}
        elif data.get("call_type") == "group":
            # send notification to group
            return {"status": "successful", "message": "send notifications to group"}
        else:
            dbService.drop()
            return {"status": "failed", "message": "invalid call type"}
    else:
        dbService.drop()
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequest(data):
    if data is not None:
        return data.get("access_token") is not None and data.get("token_owner") is not None and \
               data.get("call_type") is not None and data.get("call_name") is not None
    else:
        return False
