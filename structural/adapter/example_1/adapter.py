from usa_socket import IUSASocket

class Adapter(IUSASocket):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket


    
    def voltage(self):
        return 110
    
    def live(self):
        return self.__socket.live()
    
    def neutral(self):
        return self.__socket.neutral()
    
    