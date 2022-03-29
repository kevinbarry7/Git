def celsius(f_num):
    c_num = ((f_num - 32) * (5/9))
    return c_num

def fahrenheit(c_num):
    f_num = (c_num * (9/5) + 32)
    return f_num

cels = celsius(72)
print("{} degrees F = {} degrees C".format(72, cels))


fahr = fahrenheit(37)
print("{} degrees C = {} degrees F".format(37, fahr))

n = 1
while (n<=5):
    print("n =", n)
    n = n + 1
print("Loop finished")

for n in range(1, 5):
    print("n =", n)
print("Loop Finished")

for n in range(1, 4):
    for j in ["a", "b", "c"]:
        print("n = ", n, "and j = ", j)
for n in range(2, 10):
    print("n = ", n)
print("------------")


n = 2
while (n <= 10):
    print("n = ", n)
    n = n + 1
print("Loop finished!!!")

def doubles(num):
    for n in range(1,4):
        total = (num * num)
doubles(2)
