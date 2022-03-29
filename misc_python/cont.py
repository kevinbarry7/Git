for n in range(1, 51):
    if n % 3 == 0:
        print("{} is divisible by 3".format(n))
        continue
    else: n += 1

print("Done!!!")