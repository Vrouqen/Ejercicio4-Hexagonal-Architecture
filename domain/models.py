# Domain entity

from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    id: int
    name: str
    grades: List[float]
