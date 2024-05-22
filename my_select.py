from sqlalchemy import func, cast, Integer, and_
from models import *
from connect_db import session

def select_1():
    return session.query(Student.fullname, cast(func.avg(Grade.grade), Integer)\
        .label('avg_grade'))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc())\
        .limit(5).all()

def select_2(subject_id):
    return session.query(Student.fullname, cast(func.avg(Grade.grade), Integer)\
        .label('avg_grade'))\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc()).first()

def select_3(subject_id):
    return session.query(Student.group_id, cast(func.avg(Grade.grade), Integer)\
        .label('avg_grade'))\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.group_id).all()

def select_4():
    return session.query(cast(func.avg(Grade.grade), Integer)\
        .label('avg_grade')).first()

def select_5(teacher_id):
    return session.query(Subject.name)\
        .join(Subject.teacher)\
        .filter(Teacher.id == teacher_id).all()

def select_6(group_id):
    return session.query(Student.fullname)\
        .filter_by(group_id=group_id).all()

def select_7(group_id, subject_id):
    return session.query(Student.id, Grade.grade)\
        .join(Group).filter(Group.id == group_id)\
        .join(Grade).filter(Grade.subject_id == subject_id).all()

def select_8(teacher_id):
    return session.query(cast(func.avg(Grade.grade), Integer)\
        .label('avg_grade'))\
        .join(Subject)\
        .filter(Subject.teacher_id == teacher_id).first()


def select_9(student_id):
    return session.query(Grade.subject_id)\
        .filter_by(student_id=student_id).distinct().all()

def select_10(student_id, teacher_id):
    return session.query(Subject.name)\
        .join(Grade, and_(Subject.id == Grade.subject_id, Grade.student_id == student_id))\
        .filter(Subject.teacher_id == teacher_id).distinct().all()


if __name__ == "__main__":

    print("Select 1:")
    print(select_1())

    print("Select 2:")
    print(select_2(subject_id=1))  # замініть на потрібний ід предмету

    print("Select 3:")
    print(select_3(subject_id=1))  # замініть на потрібний ід предмету

    print("Select 4:")
    print(select_4())

    print("Select 5:")
    print(select_5(teacher_id=1))  # замініть на потрібний ід викладача

    print("Select 6:")
    print(select_6(group_id=1))  # замініть на потрібний ід групи

    print("Select 7:")
    print(select_7(group_id=1, subject_id=1))  # замініть на потрібні ід групи і предмета

    print("Select 8:")
    print(select_8(teacher_id=1))  # замініть на потрібний ід викладача

    print("Select 9:")
    print(select_9(student_id=1))  # замініть на потрібний ід студента

    print("Select 10:")
    print(select_10(student_id=1, teacher_id=1))  # замініть на потрібні ід студента і викладача
