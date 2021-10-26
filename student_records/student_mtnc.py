#!/usr/bin/env python3

import validation as v

# def list(student):
#     if len(student) == 0:
#         print("There are no students in the list.\n")
#         return
#     else:
#         i = 1
#         for student in student_list:
#             row = student
#             print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
#             i += 1
#         print()


def add(students, next_student_id):
    """
    docstring
    """

    first_name = v.get_string(prompt='Please enter the student\'s First Name: ').title()
    last_name = v.get_string(prompt='Please enter the student\'s Last Name: ').title()

    students.append([next_student_id, first_name, last_name])

    print(f'Student ID #{next_student_id} {first_name} {last_name} was added.')


#
# def delete(movie_list):
#     number = int(input("Number: "))
#     if number < 1 or number > len(movie_list):
#         print("Invalid movie number.\n")
#     else:
#         movie = movie_list.pop(number - 1)
#         print(movie[0] + " was deleted.\n")
#
# def update():
#     print()