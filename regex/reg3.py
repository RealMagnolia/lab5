import re
txt = input()
x = re.findall("[a-z]+_", txt)
print(x)

#input: my_name_is_Dana oooooooo
#output: ['my_', 'name_', 'is_']