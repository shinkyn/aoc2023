import math

f = open("input.txt", "r")
strings = [str(i) for i in f.read().split('\n')]


class Bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


# print(strings)
cogs = {}
# good thing there is no triple gears
for s, i in zip(strings, range(0, len(strings))):
    num = ''
    for ch, j in zip(s, range(0, len(s))):
        last_digit = False
        if ch.isdigit():
            num += ch
            last_digit = j + 1 == len(s)
        if not ch.isdigit() or last_digit:
            if len(num):
                if ch != '.' and not last_digit:
                    # print('case !.', num, ch, i, j)
                    if ch == '*':
                        if i not in cogs:
                            cogs[i] = {j: []}
                        if j not in cogs[i]:
                            cogs[i][j] = []
                        cogs[i][j].append(int(num))
                else:
                    # print('case .', num, ch, i, j)
                    # todo: make it compare/match substrings instead of double loop every char in area
                    for ci in range(max(0, i - 1), min(len(strings), i + 2)):
                        for cj in range(max(0, j - len(num) - 1), min(len(s), j + 1)):
                            # print('check', strings[ci][cj], num, ci, cj)
                            if strings[ci][cj] != '.' and not strings[ci][cj].isdigit():
                                # print('added', num, i, j)
                                if strings[ci][cj] == '*':
                                    if ci not in cogs:
                                        cogs[ci] = {cj: []}
                                    if cj not in cogs[ci]:
                                        cogs[ci][cj] = []
                                    cogs[ci][cj].append(int(num))
                num = ''
# second run to output colorized * where it connects gears
for s, i in zip(strings, range(0, len(strings))):
    num = ''
    for ch, j in zip(s, range(0, len(s))):
        last_digit = False
        if ch.isdigit():
            num += ch
            last_digit = j + 1 == len(s)
        if not ch.isdigit() or last_digit:
            if len(num):
                added = False
                if ch != '.' and not last_digit:
                    added = True
                else:
                    for ci in range(max(0, i - 1), min(len(strings), i + 2)):
                        for cj in range(max(0, j - len(num) - 1), min(len(s), j + 1)):
                            if strings[ci][cj] != '.' and not strings[ci][cj].isdigit():
                                added = True
                color = Bcolors.WARNING
                if added:
                    color = Bcolors.OKGREEN
                if last_digit:
                    ch = ''
                print(f"{color}{num}{Bcolors.ENDC}", end="")
                num = ''
            match ch:
                case '*':
                    un = ''
                    if i in cogs and j in cogs[i] and len(cogs[i][j]) > 1:
                        un = Bcolors.UNDERLINE
                    print(f"{Bcolors.OKBLUE}{un}{ch}{Bcolors.ENDC}", end="")
                case '.':
                    print(ch, end="")
                case _:
                    print(f"{Bcolors.FAIL}{ch}{Bcolors.ENDC}", end="")
    print()
s = 0
for x in cogs.values():
    for y in x.values():
        if len(y) > 1:
            s += math.prod(y)
print(s)
