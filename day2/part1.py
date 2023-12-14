import re

f = open("input.txt", "r")
strings = [str(i) for i in f.read().split('\n')]

m = {'red': 12, 'green': 13, 'blue': 14}
s = 0
for st in strings:
    nl = re.findall(r'Game (\d+): (.*)', st)
    print(st, nl)
    sets = nl[0][1].split('; ')
    print(sets)
    cur = int(nl[0][0])
    for a in sets:
        dice = a.split(', ')
        for d in dice:
            a = d.split()
            if int(a[0]) > m[a[1]]:
                print(d)
                cur = 0
    s += cur
print(s)
