import mysql.connector
from utils.Generation import generateToken
from database.actions import FetchAllTechniker, LoginAction, AddUserToken, CheckPermissionViaToken, InsertTechniker
from database.actions import UpdateTechniker, FetchTechniker, AddTask, GetFreeTechnikerWithPreferedTask
from database.actions import GetFreeTechnikerWithAusbildungForTask, AcceptTask, SetTechnikerAuftrag
from database.actions import ListAllTasksForTechniker, FinishTask, GetActiveTaskOfTechniker
from database.actions import FetchAllOnlinetechniker, FetchOnlineTechnikerWithoutTask


class DatabaseService(object):
    conn = None

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="10.11.0.3",
            password="LgdQJUcBKd5AEtaF",
            user="wr-paging",
            database="wr-paging",
            auth_plugin="mysql_native_password"
        )

    def drop(self):
        self.conn.close()

    def FetchAllTechniker(self):
        return FetchAllTechniker.execute(self.conn)

    def Login(self, vorname, nachname, password):
        status = LoginAction.execute(self.conn, vorname=vorname, name=nachname, pwd=password)
        if status:
            token = generateToken()
            owner = vorname + '.' + nachname
            AddUserToken.execute(self.conn, owner=owner, token=token)
            return True, token
        else:
            return False, None

    def CheckPermissionViaToken(self, token, owner):
        return CheckPermissionViaToken.execute(self.conn, token, owner)

    def InsertTechniker(self, user_info):
        InsertTechniker.execute(self.conn, user_info=user_info)

    def UpdateTechniker(self, user, category, value):
        UpdateTechniker.execute(conn=self.conn, token_owner=user, category=category, value=value)

    def FetchTechniker(self, username):
        return FetchTechniker.execute(self.conn, username)

    def addTask(self, name, aufgabe, owner, date=None, treffpunkt=None):
        AddTask.execute(self.conn, name, aufgabe, owner, date, treffpunkt)

    def getFreeTechnikerWithPreferedTask(self, aufgabe):
        return GetFreeTechnikerWithPreferedTask.execute(self.conn, aufgabe)

    def getFreeTechnikerWithAusbildungForTask(self, ausbildung):
        return GetFreeTechnikerWithAusbildungForTask.execute(self.conn, ausbildung)

    def acceptTask(self, auftragsID):
        AcceptTask.execute(self.conn, auftragsID)

    def updateTechnikerTask(self, taskID, username):
        SetTechnikerAuftrag.execute(self.conn, taskID, username)

    def listAllAuftraegeForTechniker(self, technikerID):
        return ListAllTasksForTechniker.execute(self.conn, technikerID)

    def finishTask(self, taskID):
        FinishTask.execute(self.conn, taskID)

    def getActiveTaskOfUser(self, username):
        return GetActiveTaskOfTechniker.execute(self.conn, username)

    def getOnlineTechniker(self):
        return FetchAllOnlinetechniker.execute(self.conn)

    def getOnlineTechnikerWithoutTask(self):
        return FetchOnlineTechnikerWithoutTask.execute(self.conn)
