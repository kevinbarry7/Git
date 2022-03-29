nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!!!')
        continue
        # break
    print(num)
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

for num in range(1, 10):
    print(num)


def hello_func():
    print('hello function!')


hello_func()
# DRY (Don't Repeat Yourself)


def hello_func():
    return('hello function!1')


def hello_func(greeting, name='Kevin'):
    return '{}, {}.'.format(greeting, name)


print(hello_func('hello!'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

big = min('Hello world')
print(big)
