from fastapi import APIRouter
from fake_data.fake_data import get_fake_courses
from typing import List

router = APIRouter()

@router.get('/course')
def get_course(search:str="") -> list:
   courses =  get_fake_courses(20)
   filter_courses = []
   for course in courses:
      if search in course.id or search in course.name or search in course.class_id:
         filter_courses.append(course)
      else:
         for teacher in course.teacher_list:
            if search in teacher.name:
               filter_courses.append(teacher)
   return filter_courses