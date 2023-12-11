data = [x.strip() for x in open('aoc2023-11-input.txt')]

def pprint(s):
    print(min(s, key = lambda t: t[0]))
    r0, _ = min(s, key = lambda t: t[0])
    r1, _ = max(s, key = lambda t: t[0])
    _, c0 = min(s, key = lambda t: t[1])
    _, c1 = max(s, key = lambda t: t[1])

    print()
    for row in range(r0, r1+1):
        line = ''
        for col in range(c0, c1+1):
            if (row, col) in s:
                line = line + "#"
            else:
                line = line + "."
        print(line)
    print()

def getstars():
    stars = []
    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == '#':
                stars.append((r,c))
    return(stars)

def extend(themap):
    swellrows = []
    swellcols = []    
    for r, row in enumerate(themap):
        if all([x == '.' for x in row]):
            swellrows.append(r)

    for c, ch in enumerate(themap[0]):
        if all([x == '.' for r in range(0, len(themap)) for x in themap[r][c]]):
            swellcols.append(c)
    return(swellrows, swellcols)

def swell(ss, amount, swellrows, swellcols):
    for s, star in enumerate(ss):
        rs, cs = ss[s]
        for r, row in enumerate(swellrows):
            if row < rs:
                ss[s] = (rs + (r+1)*amount, cs)
        rs, cs = ss[s]
        for c, col in enumerate(swellcols):
            if col < cs:
                ss[s] = (rs, cs + (c+1)*amount)
    return(ss) 

srows, scols = extend(data)

def dist(a, b):
    return(abs(a[0] - b[0]) + abs(a[1] - b[1]))

def part1(stars1):
    stars1 = swell(stars1, 1, srows, scols)
    s1dist = []
    for i, star1 in enumerate(stars1):
        for star2 in stars1[i+1:]:
            s1dist.append(dist(star1, star2))
    return(sum(s1dist))

def part2(stars2):
    stars2 = swell(stars2, 1000000-1, srows, scols)
    s2dist = []
    for i, star1 in enumerate(stars2):
        for star2 in stars2[i+1:]:
            s2dist.append(dist(star1, star2))
    return(sum(s2dist))

print('Day 11, part 1:', part1(getstars()))

print('Day 11, part 2:', part2(getstars()))