from student import Student
from teacher import Teacher
from person_type import PersonType


class PersonFactory:

    @staticmethod
    def get_person(person_type: PersonType):
        if person_type == PersonType.STUDENT:
            return Student()
        if person_type == PersonType.TEACHER:
            return Teacher()
        else:
            raise RuntimeError("Invalid person type")

