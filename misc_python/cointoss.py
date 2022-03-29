from random import randint

heads = 0
tails = 0

for trial in range(0, 10000):
    while randint(0,1) ==0:
        tails += 1
    heads += 1
print(heads)
print(tails)
print("heads / tails =  ", heads/tails)

oone = ttwo = tthree = ffour = ffive = ssix = 0
for toss in range(0, 10000):
    dice = randint(1, 6)
    if dice == 1:
        oone += 1
    elif dice == 2:
        ttwo += 1
    elif dice == 3:
        tthree += 1
    elif dice == 4:
        ffour += 1
    elif dice == 5:
        ffive += 1
    else: 
        ssix += 1
print(" The throws of the die were as follows: ")
print()
print("one - {}, two - {}, three - {}, four - {}, five - {}, six - {}".format(oone, ttwo, tthree, ffour, ffive, ssix))
