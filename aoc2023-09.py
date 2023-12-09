data = [[int(x) for x in line.split()] for line in open('aoc2023-09-input.txt')]

def wrap(lists):
    # Part 1:
    lists[-1].append(0)
    # Part 2:
    lists[-1] = [0] + lists[-1]

    l = 2
    while l < len(lists)+1:
        # Part 1:
        add = lists[-l+1][-1]
        lists[-l].append(lists[-l][-1] + add)
        # Part 2:
        sub = lists[-l+1][0]
        lists[-l] = [lists[-l][0] - sub] + lists[-l]

        l += 1
    return(lists)

def run(line):
    calc = [line]
    while True:
        if all((x == 0 for x in calc[-1])):
            return(calc)
        last = calc[-1]
        i = 0
        diffs = []
        while i < len(last)-1:
            diffs.append(last[i+1] - last[i])
            i += 1
        calc.append(diffs)

ans1 = 0
ans2 = 0
for line in data:
    calc = wrap(run(line))
    ans1 += calc[0][-1]
    ans2 += calc[0][0]
print('Day 9, part 1:', ans1)
print('Day 9, part 2:', ans2)
