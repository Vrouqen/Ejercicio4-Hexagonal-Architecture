# Domain services

from typing import List

class GradeCalculatorService:
    # Port interface
    def calculate_average(self, grades: List[float]) -> float:
        if not grades:
            return 0.0
        return sum(grades) / len(grades)
