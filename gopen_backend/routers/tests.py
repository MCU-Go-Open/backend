from fastapi import APIRouter
from fake_data.fake_data import get_fake_courses

router = APIRouter()

@router.get('/course')
def get_course():
   return get_fake_courses(20)