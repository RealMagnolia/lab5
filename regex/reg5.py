import re
txt = input()
x = re.findall("^a.*?b$", txt)
print(x)

#input: 1.ahahahb  2.ajajaj
#output: 1.['ahahahb']  2.[]
