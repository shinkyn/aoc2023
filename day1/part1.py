import re

f = open("input.txt", "r")
strings = [str(i) for i in f.read().split('\n')]

s = 0
for st in strings:
    nl = re.sub(r'\D', '', st)
    s += int(nl[0] + nl[-1])
print(s)
