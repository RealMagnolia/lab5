import re
txt = input()
x = re.findall("ab*", txt)
print(x)


#input: ab a0 abbb kk baa ab aabab
#ouput: ['ab', 'a', 'abbb', 'a', 'a', 'ab', 'a', 'ab', 'ab']