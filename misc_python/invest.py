def invest(amount, rate, time):
    print("principal amount: ", amount)
    print("annual rate of return: ", rate)
    for y in range(1,time+1):
        amount = (amount * (rate + 1))
        print("year {}: {}".format (y, amount))




invest(100, .05, 8)
print()
invest(2000, .025, 5)
