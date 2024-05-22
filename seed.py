from faker import Faker
from random import randint, choice
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from connect_db import engine
fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(name=fake.company()) for _ in range(3)]
session.add_all(groups)
session.commit()

students = [Student(fullname=fake.name(), group_id=choice(groups).id) for _ in range(randint(30, 50))]
session.add_all(students)
session.commit()

teachers = [Teacher(fullname=fake.name()) for _ in range(randint(3, 5))]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher_id=choice(teachers).id) for _ in range(randint(5, 8))]
session.add_all(subjects)
session.commit()

for student in students:
    for _ in range(randint(10, 20)):
        subject = choice(subjects)
        grade = Grade(
            student_id=student.id,
            subject_id=subject.id,
            grade=randint(1, 10),
            date=fake.date_between(start_date='-1y', end_date='today')
        )
        session.add(grade)

session.commit()
