from database.DatabaseService import DatabaseService


class TechnikerSelector(object):

    def __init__(self, dbService: DatabaseService):
        self.dbService = dbService

    def getTechniker(self, aufgabe):
        aufgabenSpecific = self.dbService.getFreeTechnikerWithPreferedTask(aufgabe=aufgabe)
        if len(aufgabenSpecific) is not 0:
            return aufgabenSpecific

        ausbildungsSpecific = self.dbService.getFreeTechnikerWithAusbildungForTask(ausbildung=aufgabe)
        if len(aufgabenSpecific) is not 0:
            return ausbildungsSpecific
        return None

