import os

path = "C:\Users\Руслан\Desktop\pp labs\lab6\lab6\DirAndFiles\daf4.txt"

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))