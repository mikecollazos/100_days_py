import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']


student_scores = {student:(random.randint(0, 100)) for student in names}
print(student_scores.items())


passed_students = {student:value for student,value in student_scores.items() if value > 60}
print(passed_students)


