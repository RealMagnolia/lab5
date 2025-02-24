import re
txt = input()
x = re.findall("[A-Z][a-z]+", txt)
print(x)

#input: DS Math Drives Me CRAZY frrrrr
#output: ['Math', 'Drives', 'Me']