# Student adapter

from domain.models import Student

class StudentRepositoryMemory:
    def __init__(self):
        self.students = {
            1: Student(id=1, name="Juan", grades=[10, 9, 8]),
            2: Student(id=2, name="Ana", grades=[7, 7, 6])
        }

    def get_by_id(self, student_id: int) -> Student:
        return self.students.get(student_id)
