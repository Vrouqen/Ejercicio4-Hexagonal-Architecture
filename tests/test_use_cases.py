# Test use cases

from application.use_cases import CalculateStudentAverageUseCase
from domain.services import GradeCalculatorService
from domain.models import Student

class FakeRepo:
    def get_by_id(self, student_id):
        return Student(id=student_id, name="Test", grades=[5, 6, 7])

def test_average():
    repo = FakeRepo()
    calculator = GradeCalculatorService()
    use_case = CalculateStudentAverageUseCase(repo, calculator)
    assert use_case.execute(1) == 6.0
    print("Test passed successfully")

if __name__ == "__main__":
    test_average()
