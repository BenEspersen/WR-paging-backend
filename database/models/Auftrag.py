class Auftrag(object):
    ID = None
    Name = None
    Aufgabe = None
    Status = None
    technikerID = None
    Date = None
    Treffpunkt = None
    Timestamp = None

    def __init__(self, arr):
        self.ID = arr[0]
        self.Name = arr[1]
        self.Aufgabe = arr[2]
        self.Status = arr[3]
        self.technikerID = arr[4]
        self.Date = arr[5]
        self.Treffpunkt = arr[6]
        self.Timestamp = arr[7]