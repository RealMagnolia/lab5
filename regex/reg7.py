import re
txt = input()

def snakeToCamel(text):
    x = re.findall("[a-z]+", txt)
    help = ""
    for i in x:
        help += i[0].upper() + i[1:len(i)]
    return help

print(snakeToCamel(txt))

#input: nothings_new
#output: NothingsNew