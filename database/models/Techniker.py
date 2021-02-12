class TechnikerModel(object):
    ID = None
    Name = None
    Vorname = None
    Klasse = None
    Schluessel = None
    Ausbildungen = None
    Aufgaben = None
    aktuellerAuftrag = None
    timestamp = None

    def __init__(self, arr):
        self.ID = arr[0]
        self.Name = arr[1]
        self.Vorname = arr[2]
        self.Klasse = arr[3]
        self.Schluessel = arr[4]
        self.Ausbildungen = arr[5]
        self.Aufgaben = arr[6]
        self.aktuellerAuftrag = arr[7]
        self.timestamp = arr[8]
