import socket
import threading
import json

from database.DatabaseService import DatabaseService
from websockets import NoteSocket


class WebsocketWrapper(object):

    def handle_action(self, data, conn, client_address):
        if data["action"] == "loadNotes":
            print("nigga")
            conn.send(str({"status": "successful", "notes": NoteSocket.loadNotes(), "type": "notes"}).encode(encoding="utf-8"))
        elif data["action"] == "replaceNotes":
            NoteSocket.replaceNotes(data["notes"])
            for addr in self.addressList:
                if addr != client_address:
                    self.globalSocket.sendto(
                        str({"status": "successful", "notes": NoteSocket.loadNotes(), "type": "notes"}).encode(encoding="utf-8"),
                        address=addr)
        else:
            conn.send(str({"status": "failed", "message": "dies ist keine registrierte action"}).encode(encoding="utf-8"))

    def __init__(self):
        self.Threadcounter = 0
        self.status = False
        self.addressList = []

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 5001))
            s.listen()
            print("Started socket server...")
            self.globalSocket = s
            while True:
                if self.status:
                    s.close()
                    break
                conn, addr = s.accept()
                self.Threadcounter += 1
                t = threading.Thread(self.connection_thread(conn, addr))
                t.start()

    def quit(self):
        self.status = True

    def connection_thread(self, conn, addr):
        with conn:
            print("connected with", addr)
            print("number of active connection threads:", self.Threadcounter)
            self.addressList.append(addr)
            while True:
                try:
                    data = bytes(conn.recv(2048))
                    js = data.decode(encoding="utf-8").replace("\'", "\"")
                    message = json.loads(js)
                    if message["action"] is not None and message["access_token"] is not None and message[
                        "token_owner"] is not None:
                        dbService = DatabaseService()
                        if dbService.CheckPermissionViaToken(message["access_token"], message["token_owner"]):
                            dbService.drop()
                            self.handle_action(message, conn, addr)
                        else:
                            conn.send(
                                str({"status": "failed", "message": "login fehlgeschlagen"}).encode(encoding="uft-8"))
                    else:
                        conn.close()
                        self.Threadcounter -= 1
                        self.addressList.remove(addr)
                        break
                except:
                    conn.close()
                    self.Threadcounter -= 1
                    self.addressList.remove(addr)
                    break
