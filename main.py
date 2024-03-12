print('Finding Maximum Number in a List ! ')

student_marks = input('Enter the marks separated by comma : ').split(',')

for n in range(0, len(student_marks)):
    student_marks[n] = student_marks[n]
print(student_marks)

m = 0

for i in student_marks:
    if m < int(i):
        m = int(i)

print(f'The highest mark is {m}')
