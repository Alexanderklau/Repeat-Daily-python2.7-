from asyncore import dispatcher
import socket,asyncore

class ChatServer(dispatcher):
    def handle_accept(self):
        coon.addr = self.accept()
        print()