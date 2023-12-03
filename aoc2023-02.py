data = [r.strip('\n') for r in open('aoc2023-02-input.txt')]

summ = 0
total = {'red': 12, 'green': 13, 'blue': 14}

powersum = 0

for row in data:
    few = {'red': 0, 'green': 0, 'blue': 0}
    ok = True
    id_ = int(row.split(':')[0].split(' ')[1])
    for hand in row.split(':')[1].split(';'):
        for nbr,col in [x.strip().split(' ') for x in hand.split(',')]:
            few[col] = max(few[col], int(nbr))
            if total[col] < int(nbr):
                ok = False
#                break
    if ok:
        summ = summ + id_

    ans = 1
    for item in few.keys():
        ans = ans * few[item]

    powersum = powersum + ans

print('Day 2, part 1:', summ)
print('Day 2, part 2:', powersum)