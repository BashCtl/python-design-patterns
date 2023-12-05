from iuk_connector import IUkPlugConnector
class UKElectricalSocket:

    def plug_in(self, uk_plug:IUkPlugConnector):
        print("This is a UK electrical socket")
        uk_plug.power()