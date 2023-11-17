from capital_city import CapitalCity


class Madrid(CapitalCity):

    def get_popullation(self) -> int:
        return 3200000

    def list_top_attractions(self) -> []:
        return ["Royal Palace", "Prado Museum", "Retiro Park"]
