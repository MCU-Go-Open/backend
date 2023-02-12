from faker import Faker
from models.course import Course,Teacher


fake = Faker(['zh_TW'])

def get_fake_teachers(size:int=1) -> list:
  teacher_list = []
  for _ in range(size):
    teacher_list.append(
      Teacher(fake.name(),fake.credit_card_number(),fake.random_element(elements=('main','sub')))
    )
  return teacher_list


def get_fake_courses(size:int=1) -> list:
  course_list = []
  for _ in range(size):
    course_id = fake.credit_card_number()[:5]
    course_name = fake.job()
    class_id = fake.credit_card_number()[:5]
    grade = fake.random_element(elements=('0','1','2','3','4','5'))
    type = fake.random_element(elements=(0,1,2,3))
    classroom = [fake.numerify(text='S%%%')]
    campus = [fake.random_element(elements=("桃園","台北","金門","成功"))]
    semester = fake.random_element(elements=(0,1,2))
    credits = fake.random_element(elements=(0,1,2,3))
    special_type = "fake_special_type"
    comments =  fake.sentence()
    isgraduate = fake.pybool()
    course_hash = fake.credit_card_number()
    super_hash = fake.credit_card_number()
    teacher_list = get_fake_teachers(3)
    course_list.append(Course(course_id,course_name,class_id,teacher_list,grade,type,classroom,campus,semester,credits,special_type,isgraduate,comments,course_hash,super_hash)) 

  return course_list

if __name__ == "__main__":
  print(get_fake_courses(3))