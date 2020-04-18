graphic_students = ['manish','steve' ,'mohammed' ,'darpan','zulfekhar', 'sandeep','prashant']


webdev_students = []

for student in graphic_students:

    if student == 'steve':
        continue
    elif student == 'manish':
        continue
    else:
        webdev_students.append(student)

print('the lsit of Web Dev students:', webdev_students)    