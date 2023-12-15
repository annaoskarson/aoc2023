data = [x.strip() for x in open('aoc2023-13-input.txt')]

def ismirror(pattern, num, v=True, part2=False):
    if not(v): # Horizontal
        transposed = []
        for c in range(len(pattern[0])):
            row = ''.join([x[c] for x in pattern])
            transposed.append(row)
        pattern = transposed

    lefts = [x[:num] for x in pattern]
    lefts = [x[::-1] for x in lefts]
    rights = [x[num:] for x in pattern]

    mirror = []
    mirror2 = []
    if len(lefts[0]) < len(rights[0]):
        for i in range(len(lefts)):
            mirror.append(rights[i].startswith(lefts[i]))
            mirror2.extend([lefts[i][n] != rights[i][n] for n in range(len(lefts[i]))])
    else: # len(rights[0]) < len(lefts[0]):
        for i in range(len(lefts)):
            mirror.append(lefts[i].startswith(rights[i]))
            mirror2.extend([lefts[i][n] != rights[i][n] for n in range(len(rights[i]))])
    if part2:
        return(sum(mirror2) == 1)
    return(all(mirror))


def pprint(pic):
    for p in pic:
        print(p)

i = 0
ans = 0
ans2 = 0
record = {}
im = 0
while i < len(data):
    image = []
    while i < len(data) and len(data[i]) != 0:
        image.append(data[i])
        i += 1
    im += 1

    vertical = []
    horizontal = []
    v2 = []
    h2 = []
    # Testa vertikalt och horisontellt
    for v in range(1, len(image[0])):
        if ismirror(image, v):
            vertical.append(v)
        elif ismirror(image, v, True, True):
            v2.append(v)
    for h in range(1, len(image)):
        if ismirror(image, h, False):
            horizontal.append(h)
        elif ismirror(image, h, False, True):
            h2.append(h)
    record[im] = (image, vertical, horizontal)
    i +=1
    ans += sum(vertical) + sum([100 * x for x in horizontal])
    ans2 += sum(v2) + sum([100 * x for x in h2])

print('Day 13, part 1:', ans)

print('Day 13, part 2:', ans2)
