# Application (Uses cases) 

from domain.services import GradeCalculatorService

class CalculateStudentAverageUseCase:
    def __init__(self, repository, calculator: GradeCalculatorService):
        self.repository = repository
        self.calculator = calculator

    def execute(self, student_id: int) -> float:
        student = self.repository.get_by_id(student_id)
        return self.calculator.calculate_average(student.grades)
