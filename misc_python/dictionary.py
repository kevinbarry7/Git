
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['courses'])
print(student['age'])
for key, value in student.items():
    print(key, value)


myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

cigniti = {'name': 'Harish', 'hourly': 80, 'Dec': 160,
			'name': 'Vittal', 'hourly': 40, 'Dec': 85}
for v in cigniti.items():
	print(v)
