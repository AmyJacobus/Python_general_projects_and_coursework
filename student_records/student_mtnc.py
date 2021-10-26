#!/usr/bin/env python3

import validation as v

def list(students):
    if len(students) == 0:
        print("There are no students in the list.\n")
        return
    else:
        i = 1
        for student in students:
            row = student
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
            i += 1
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


def find_student_index(students, next_student_id):

    for student in students:
        if student[0] == next_student_id
         return students.index(student) # This will return the student index to me

    return -1 # Would never be a valida index, meaning the student is not in the list

def delete(students):

    print()
    print('Delete Student')
    print('_' * 50)

    if len(students) == 0:
        print("There are no students in the list.\n")
        return

     student_id = v.get_num(prompt='Please enter the Student ID to be deleted: ')

    student_index = find_student_index(students, student_id)
    if student_index == -1:
        print('Student not found')
        return

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