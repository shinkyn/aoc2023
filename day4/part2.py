import re

f = open("input.txt", "r")
strings = [str(i) for i in f.read().split('\n')]

cards = [1 for x in range(len(strings))]
for s in strings:
    nl = re.findall(r'Card\s+(\d+): (.*)', s)
    card = int(nl[0][0])-1
    parts = nl[0][1].split('|')
    w_nums = [int(i) for i in parts[0].split()]
    nums = [int(i) for i in parts[1].split()]
    cnt = len(set(nums).intersection(w_nums))
    for i in range(card + 1, card + cnt + 1):
        cards[i] += cards[card]
print(sum(cards))
