from AoC2023.colors import Bcolors

f = open("input.txt", "r")
strings = [str(i) for i in f.read().split('\n')]

# print(strings)
myl = []
for s, i in zip(strings, range(0, len(strings))):
    num = ''
    for ch, j in zip(s, range(0, len(s))):
        last_digit = False
        if ch.isdigit():
            num += ch
            last_digit = j+1 == len(s)
        if not ch.isdigit() or last_digit:
            if len(num):
                added = False
                if ch != '.' and not last_digit:
                    # print('case !.', num, ch, i, j)
                    myl.append(int(num))
                    added = True
                else:
                    adj = False
                    # print('case .', num, ch, i, j)
                    # todo: make it compare/match substrings instead of double loop every char in area
                    for ci in range(max(0, i - 1), min(len(strings), i + 2)):
                        for cj in range(max(0, j - len(num) - 1), min(len(s), j + 1)):
                            # print('check', strings[ci][cj], num, ci, cj)
                            if strings[ci][cj] != '.' and not strings[ci][cj].isdigit():
                                adj = True
                                added = True
                                # print('added', num, i, j)
                                myl.append(int(num))
                                break
                        if adj:
                            break
                color = Bcolors.WARNING
                if added:
                    color = Bcolors.OKGREEN
                if last_digit:
                    ch = ''
                print(f"{color}{num}{Bcolors.ENDC}", end="")
                num = ''
            if ch != '.':
                print(f"{Bcolors.FAIL}{ch}{Bcolors.ENDC}", end="")
            else:
                print(ch, end="")
    print()
# print(myl)
print(sum(myl))
