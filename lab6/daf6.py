import os

path =  r"C:\Users\Руслан\Desktop\pp labs\lab6\DirAndFiles\daf6Files"

if not os.path.exists(path):
   os.makedirs(path)

A = ord('A')
base = 'ex06_A-Z_files\\{}.txt'
for i in range(A, A+26):
    f = open(base.format(chr(i)), 'w')