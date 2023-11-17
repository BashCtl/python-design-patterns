from capital_city import CapitalCity


class London(CapitalCity):

    def get_popullation(self) -> int:
        return 8900000

    def list_top_attractions(self) -> []:
        return ["Tower Bridge", "Buckingham Palace", "Big Ben"]
