from iusplug_connector import IUSPlugConnector


class USPlugConnector(IUSPlugConnector):

    def power(self):
        print("US plug")