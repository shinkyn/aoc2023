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
    lv = {'red': [], 'green': [], 'blue': []}
    for a in sets:
        dice = a.split(', ')
        for d in dice:
            a = d.split()
            lv[a[1]].append(int(a[0]))
    print(lv, max(lv['red']), max(lv['green']), max(lv['blue']))
    s += max(lv['red']) * max(lv['green']) * max(lv['blue'])
print(s)
