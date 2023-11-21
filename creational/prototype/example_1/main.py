from teacher import Teacher
from student import Student

# client


def main():
    teacher = Teacher("Mad Max", "Killing Assholes")
    teacher_clone = teacher.clone()
    teacher_clone.display()

    student = Student("John Wick", teacher_clone)
    student_clone = student.clone()
    student_clone.display()

    # modify teacher clone
    teacher_clone.set_course("Punching arrogant people")
    student_clone.display()


if __name__ == "__main__":
    main()
