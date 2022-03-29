def factor(number):
    for n in range(1, number + 1):
        if number % n == 0:
            print("{} is a divisor of {}".format(n, number))
    n +=1

number = int(input("Enter a positive number: "))

factor(number)
