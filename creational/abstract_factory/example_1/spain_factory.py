from capital_city import CapitalCity
from international_factory import InternationalFactory
from spanish import Spanish
from language import Language
from madrid import Madrid


class SpainFactory(InternationalFactory):

    def create_language(self) -> Language:
        return Spanish()
    
    def create_capital(self) -> CapitalCity:
        return Madrid()