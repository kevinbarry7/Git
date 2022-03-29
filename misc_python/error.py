def errortest():
    number = int(input("Enter a non-zero integer: "))
    print("The number you entered was {}".format(number))

try:
    errortest()

except ValueError:
    print("Try again!!!.")
    errortest()

