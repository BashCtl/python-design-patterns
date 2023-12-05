from usplug_connector_imp import USPlugConnector
from uk_socket import UKElectricalSocket
from us_to_uk_adapter import UStoUkPlugAdapter

def main():
    us_plug = USPlugConnector()
    uk_electrical_socket = UKElectricalSocket()
    uk_adapter = UStoUkPlugAdapter(us_plug)
    uk_electrical_socket.plug_in(uk_adapter)


if __name__ == '__main__':
    main()