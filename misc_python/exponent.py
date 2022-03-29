def square(number):
    sqr_num = number ** 2
    return sqr_num

def return_difference(num1, num2):
    return num1 - num2

def cube(num7):
    cube_num = (num7*num7*num7)
    return cube_num

def multiply(num3, num4):
    mult_num = (num3 * num4)
    return mult_num


x = float(input("Please enter a base: "))
y = float(input("Please enter an exponent: "))
result = (x ** y)
print("{} to the power of {} = {} ".format(x, y, result))

input_num = 5
output_num = square(input_num)
print(output_num)

print(return_difference(5, 3))

print(cube(2))

print(multiply(2, 5))
