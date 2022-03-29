import random
for i in range(10):
    x = random.random()
    x = int(x=x * 10)
    print(x)

hours = 45
rate = 10


def calculate_pay(hour, rate_hr):

    if hours >= 40:
        pay = float((hours - 40)) * float((rate * 1.5)) + 400.00
    else:
        pay = hours * rate
    return pay


pay = calculate_pay(hours, rate)

print(pay)

score = 1.5


def calc_grade(score):
    if score <= 1.0 and score >= 0.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Entered score is out of range")


calc_grade(score)
