import re

f = open("input.txt", "r")
strings = [str(i) for i in f.read().split('\n')]

sm = 0
for s in strings:
    nl = re.findall(r'Card\s+(\d+): (.*)', s)
    card = nl[0][0]
    parts = nl[0][1].split('|')
    w_nums = [int(i) for i in parts[0].split()]
    nums = [int(i) for i in parts[1].split()]
    cnt = len(set(nums).intersection(w_nums))
    if cnt > 0:
        sm += pow(2, cnt-1)
print(sm)
