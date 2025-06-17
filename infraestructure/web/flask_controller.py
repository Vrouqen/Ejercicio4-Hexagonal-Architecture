# Controller adapter

from flask import Flask, jsonify
from application.use_cases import CalculateStudentAverageUseCase
from domain.services import GradeCalculatorService
from infraestructure.repositories.student_repository_memory import StudentRepositoryMemory

app = Flask(__name__)

# Configuración de dependencias
repository = StudentRepositoryMemory()
calculator = GradeCalculatorService()
use_case = CalculateStudentAverageUseCase(repository, calculator)

@app.route("/students/<int:student_id>/average", methods=["GET"])
def get_average(student_id):
    avg = use_case.execute(student_id)
    return jsonify({"student_id": student_id, "average": avg})

# Solo si ejecutas directamente
if __name__ == "__main__":
    app.run(debug=True)
