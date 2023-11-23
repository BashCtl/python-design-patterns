from person_factory import PersonFactory
from person_type import PersonType



if __name__ == "__main__":
    person_type = PersonType.STUDENT
    person = PersonFactory.get_person(person_type)
    person.person_method()