from european_socket import IEuropeanSocket


class Socket(IEuropeanSocket):

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0
