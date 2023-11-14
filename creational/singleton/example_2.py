from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ implement in child class """

class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("", 0)
        return PersonSingleton.__instance
    

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once.")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}")
        print(f"Age: {PersonSingleton.__instance.age}")


if __name__ == "__main__":

    p1 = PersonSingleton("Mike", 30)
    # p2 = PersonSingleton("David", 23)
    p1.print_data()
    p2 = PersonSingleton.get_instance()
    p2.print_data()
    print(id(p1)==id(p2))