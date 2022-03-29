cake = "wedding cake"
print(len(cake))
string1 = "bicycle"
string2 = "ride"
string3 = string1 + string2
print(string3)
print(string1, string2)
weirdname = 'bazinga'
print(weirdname[2:])
print(weirdname.upper())
word = 'bike'
first_letter = word[0]
first_letter = first_letter.upper()
print("The first letter that you entered was: ", first_letter)

misc = '5'
misc = int(misc)
print(type(misc))
out = misc * 5
print(out)

misc1 = '2.2'
misc1 = float(misc1)
print(misc1 * 3.3)

misc4 = "This is a string"
misc5 = 4
misc6 = misc4 + str(misc5)
print(misc6)

name = 'Zaphod'
num_heads = 2
num_arms = 4
print("{} has {} heads and {} arms". format(name, num_heads, num_arms))


weight = 0.2
animal = 'newt'
print("{1} kg is the weight of the {0}".format(animal, weight))
print("{weight} kg is the weight of the {animal}".format(animal = 'newt', weight = 0.4))
print(f"{weight} kg is the weight of the {animal}")

term = "The latest version of the software in the HomePod is version 2.0"
version_no = 2.0
print(term.find(str(version_no)))
