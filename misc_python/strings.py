fruit = 'banana'
print(len(fruit))

index = 0
while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index += 1

index = len(fruit) - 1
while index >= 0:
	letter = fruit[index]
	print(letter)
	index = index - 1

s = 'Monty Python'
print(s[3:8])

count = 0
for letter in fruit:
	if letter == 'a':
		count += 1
print(count)
print(str.upper(fruit))
print(str.title(fruit))
print(str.lower(fruit))
print(fruit)
print(dir(fruit))

line = 'Have a nice day'
print(line.startswith('Have'))
rep = fruit.count('a')
print(rep)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1: sppos]
print(host)

term = '’X-DSPAM-Confidence:0.8475 '
colonpos = term.find(':')
print(colonpos)

commapos = term.find(' ', colonpos)
print(commapos)

factor = term[colonpos + 1: commapos]
print(float(factor))


x = 'this is a test'
":".join(x.split())
print(x)


