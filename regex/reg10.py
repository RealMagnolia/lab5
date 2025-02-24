import re
txt = input()

def camelToSnake(txt):
    x = re.sub("([a-z])([A-Z])", r"\1_\2", txt)
    return x
print(camelToSnake(txt))