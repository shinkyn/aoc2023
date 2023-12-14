import re

f = open("input.txt", "r")
strings = [str(i) for i in f.read().split('\n')]
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reps = ['o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']

s = 0
for st in strings:
    nl = st
    print(st)
    for word, i in zip(nums, reps):
        nl = re.sub(rf"{word}", i, nl)
    print(nl)
    nl = re.sub(r'\D', '', nl)
    print(nl)
    print(nl[0] + '' + nl[-1])
    s += int(nl[0] + '' + nl[-1])
print(s)
