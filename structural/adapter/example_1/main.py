from socket_impl import Socket
from adapter import Adapter
from electric_kettle import ElectricKettle

def main():
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    kettle.boil()


if __name__ == "__main__":
    main()
    