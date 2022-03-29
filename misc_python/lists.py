def numbers(numlist):
    print()
    for n in numlist:
        if n <= 20:
            print("The number {} is less than or equal to 20".format(n))
        else:
            continue


desserts = []
desserts.append('ice cream')
desserts.append('cookies')
print(desserts)
desserts.sort()
print(desserts)
print(desserts.index('cookies'))
food = []
food = desserts[:]
print(food)
desserts.append('chocolate')
print(desserts)
print(food)
food.append('broccoli')
food.append('turnips')
print(food)
food.remove('cookies')
print(food[0:2])
breakfast = []
cookie_list = 'cookies, cookies, cookies'
breakfast = cookie_list.split(', ')
print(breakfast)


numlist = [2, 4, 8, 16, 32, 64]
numbers(numlist)

