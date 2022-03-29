from random import randint

for i in range(1, 50):
    if i % 3 == 0:
        continue
    print("Number " + str(i) + " is the current number.")

print(randint(0,1))


heads = 0
tails = 0

for trials in range(0, 100000):
    while randint(0,1) == 0:
        tails = tails + 1
    heads = heads + 1

print(heads)
print(tails)

print("heads / tails = ", heads/tails)
print(i)
