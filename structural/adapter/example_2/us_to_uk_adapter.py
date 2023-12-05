from uk_socket import UKElectricalSocket
from iuk_connector import IUkPlugConnector
from usplug_connector_imp import USPlugConnector

class UStoUkPlugAdapter(IUkPlugConnector):

    def __init__(self, us_plug: USPlugConnector):
        self.us_plug = us_plug


    def power(self):
        self.us_plug.power()