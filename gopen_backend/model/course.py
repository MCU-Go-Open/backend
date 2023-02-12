from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Teacher:
  name: str
  hash: str
  type: str
  def dict(self):
      return {k: str(v) for k, v in asdict(self).items()}

@dataclass
class Course:
  id: str
  name: str
  class_id: str
  teacher_list: List[Teacher]
  grade: str
  type: int
  classroom: List[str]
  campus: List[str]
  semester: int 
  credits: int
  special_type: str
  isgraduate: bool
  comments: str
  course_hash: str
  super_hash: str
  
  def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}



