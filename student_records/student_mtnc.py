#!/usr/bin/env python3

import validation as v

def list(students):
    if len(students) == 0:
        print("There are no students in the database.\n")
        return

    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s}")
    print('-'*4, '_'*20, '_'*20)

    for student in students:
        print(f'{student[0]:4d}  {student[1]:20s} {student[2]:20s}')

    print()


def add(students, next_student_id):
    """
    docstring
    """
    print()
    print('Add Student')
    print('_' * 50)

    first_name = v.get_string(prompt='Please enter the student\'s First Name: ').title()
    last_name = v.get_string(prompt='Please enter the student\'s Last Name: ').title()
    print()

    students.append([next_student_id, first_name, last_name])

    print(f'Student ID #{next_student_id} {first_name} {last_name} was added.')


def find_student_index(students, student_id):

    for student in students:
        if student_id == student[0]:
            return students.index(student)

    return -1


def delete(students):

    print()
    print('Delete Student')
    print('_' * 50)

    if len(students) == 0:
        print("There are no students in the database.\n")
        return

    student_id = input('Please enter the Student ID you would like to delete: ')

    student_index = find_student_index(students, student_id)
    # print(student_id)#test
    if student_index == -1:
        print(f'Student ID #{student_id} not found.')
        return

    student = students[student_index] #  I have the student now

    confirm = input(f'Please confirm that you want to delete student ID# {student_id}'
          f' {student[1]} {student[2]}')

    student = students[student_index]

    print(f'Do you want do delete the student ID # {student[0]} {student[1]} {student[2]}')
    user_input = input('Y=Yes and N=No').lower()
    if user_input in ['no','n']:
        print('Delete has been cancelled')
        return

    students.pop(student_index)
    print(f'Student ID # {student[0]} {student[1]} {student[2]} was deleted.')


# def update():
#     print()