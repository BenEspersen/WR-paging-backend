from flask import request
from database.DatabaseService import DatabaseService


def handler():
    data = request.json
    if not checkRequestBody(data):
        return {"status": "error", "message": "your json request body is wrong"}
    usernameArray = str(data.get("username")).split(".")
    if len(usernameArray) != 2:
        return {"status": "failed", "message": "username must contain a dot"}
    service = DatabaseService()
    loginStatus = service.Login(vorname=usernameArray[0], nachname=usernameArray[1], password=data.get("password"))
    service.drop()
    if loginStatus[0]:
        return {"status": "successful", "message": "login successful", "token": loginStatus[1]}
    else:
        return {"status": "failed", "message": "login credentials wrong"}


def checkRequestBody(data):
    if data is not None:
        return data.get('username') is not None and data.get('password') is not None
    else:
        return False
