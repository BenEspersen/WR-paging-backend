from database.DatabaseService import DatabaseService


class TechnikerSelector(object):

    def __init__(self, dbService: DatabaseService):
        self.dbService = dbService

    def getTechniker(self, aufgabe):
        aufgabenSpecific = self.dbService.getFreeTechnikerWithPreferedTask(aufgabe=aufgabe)
        if aufgabenSpecific is not None:
            return aufgabenSpecific.ID
        ausbildungsSpecific = self.dbService.getFreeTechnikerWithAusbildungForTask(ausbildung=aufgabe)
        if ausbildungsSpecific is not None:
            return ausbildungsSpecific.ID
        return None

