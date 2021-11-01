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
        if student_id in student:
            return students.index(student)

    return -1


def delete(students):

    print()
    print('Delete Student')
    print('_' * 50)

    if len(students) == 0:
        print("There are no students in the database.\n")
        return

    student_id = int(input('Please enter the Student ID you would like to delete: '))

    student_index = find_student_index(students, student_id)
    # print(student_id)
    if student_index == -1:
        print(f'Student ID #{student_id} not found.')
        return

    student = students[student_index] #  I have the student now

    confirm = input(f'Please confirm that you want to delete student ID# {student_id}'
          f' {student[1]} {student[2]} (y=yes, n=no): ')

    if confirm in ['y','yes']:
        student = students.pop(student_index)
        print(f'Student ID # {student_id} {student[1]} {student[2]} was deleted.')
    else:
        print('Delete was cancelled!')


def update(students):
    # can't use get string, it's causing issues - you just cant use that validation here

    print()
    print('Update Student')
    print('_' * 50)

    if len(students) == 0:
        print("There are no students in the database.\n")
        return

    student_id = int(input('Please enter the Student ID to be updated: '))

    student_index = find_student_index(students, student_id)
    # print(student_id)#test
    if student_index == -1:
        print(f'Student ID #{student_id} not found.')
        return

    student = students[student_index] #  I have the student now

    confirm = input(f'Please confirm that you want to update the student ID# {student_id}'
          f' {student[1]} {student[2]} (y/n): ')

    og_name = students[student_index][1]
    og_last_name = students [student_index][2]

    if confirm in ['y', 'yes']:
        new_name = input(f'Please enter the Students First Name or press ENTER to keep {student[1]}: ')
        new_last_name = input(f'Please enter the Students First Name or press ENTER to keep {student[2]}: ')

        if new_name == '':
            print(f'No changes where made to ID #{student_id} first name.')
        else:
            students[student_index][1] = new_name

        if new_last_name == '':
            print(f'No changes where made to ID #{student_id} last name.')
        else:
            students[student_index][2] = new_last_name

        if new_name == '' and new_last_name == '':
            print('You did not type in anything, no changes were made.')
        else:
            print(f'Student ID # {student_id} {og_name} {og_last_name} was updated to'
              f'{students[student_index][1]} {students[student_index][2]} was updated.')
    else:
        print('Update was cancelled')