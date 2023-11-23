from person import IPerson

class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student"
    
    def person_method(self):
        print("Student method")