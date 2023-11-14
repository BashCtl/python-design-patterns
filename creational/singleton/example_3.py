class SingletoneLogger:

    __innstance = None

    def __init__(self):
        raise RuntimeError("This is a Singleton, invoke get_instance() instead.")
    
    @classmethod
    def get_instance(cls):
        if cls.__innstance is None:
            cls.__innstance = cls.__new__(cls)
        return cls.__innstance
    
    def log(self, ex: Exception):
        print(ex)

    def log(self, message:str):
        print(message)
    
    

if __name__ == "__main__":
    s1 = SingletoneLogger.get_instance()
    s2 = SingletoneLogger.get_instance()

    print(s1 is s2)