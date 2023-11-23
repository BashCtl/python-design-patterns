from person import IPerson


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher"

    def person_method(self):
        print("Teacher method")
    