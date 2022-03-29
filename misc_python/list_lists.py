def enrollment_stats(universities):
    students = []
    students = [item[1] for item in universities]
    tuition = []
    tuition = [item[2] for item in universities]

    return students, tuition




def mean(students, cost, size):
    avg_student = int(students/size)
    avg_cost = int(cost/size)
    return avg_student, avg_cost



def median(students, tuition):
    students.sort()
    tuition.sort()
    mid_students = len(students)
    mid_students = int(mid_students/2)
    median_students = students[mid_students]
    median_tuition = tuition[mid_students]
    return median_students, median_tuition



universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]

    ]

students, tuition = enrollment_stats(universities)
print(students)
print(tuition)
student = 0
for i in students:
    student += i
cost = 0
for j in tuition:
    cost += j

size = 0
size = len(students)
print(size)

print('Total students: ', student)
print('Total tuition: $', cost)

avg_student, avg_cost = mean(student, cost, size)
median_students, median_tuition = median(students, tuition)

print()
print('Student mean: ', avg_student)
print('Student median: ', median_students)
print()
print('Tuition mean: $', avg_cost)
print('Tuition median: $', median_tuition)