data = [x.strip() for x in open('aoc2023-16-input.txt')]

rmax = len(data)
cmax = len(data[0])

def pprint(mt, en = set()):
    pipe, dash, slash, bslash = mt
    print()
    for r in range(rmax):
        row = ''
        for c in range(cmax):
            if (r,c) in en:
                row += '#'
            elif (r,c) in dash:
                row += '-'
            elif (r,c) in pipe:
                row += '|'
            elif (r,c) in slash:
                row += '/'
            elif (r,c) in bslash:
                row += '\\'
            else:
                row += '.'
        print(row)
    print()

hl = set()
vl = set()
fs = set()
bs = set()
for r,row in enumerate(data):
    for c,ch in enumerate(row):
        if ch == '|':
            vl.add((r, c))
        elif ch == '-':
            hl.add((r, c))
        elif ch == '/':
            fs.add((r, c))
        elif ch == '\\':
            bs.add((r, c))

mirrors = vl | hl | fs | bs
mirrorstype = (vl, hl, fs, bs)

def infield(a):
    r,c,_ = a
    return(all([0 <= r< rmax, 0 <= c < cmax]))

# n, e, s, w [0, 1, 2, 3]
# Go one step, return list of new arrows.
def step(l):
    (r, c, d) = l
    nextarrows = []
    if d in [0, 2] and (r,c) in hl: # horizontal split
        nextarrows.extend([(r, c-1, 3), (r, c+1, 1)])
    elif d in [1, 3] and (r,c) in vl: # vertical split
        nextarrows.extend([(r-1, c, 0), (r+1, c, 2)])
    elif (d == 0 and (r,c) in fs) or (d == 2 and (r,c) in bs): # right
        nextarrows.extend([(r, c+1, 1)])
    elif (d == 0 and (r,c) in bs) or (d == 2 and (r,c) in fs): # left
        nextarrows.extend([(r, c-1, 3)])
    elif (d == 1 and (r,c) in fs) or (d == 3 and (r,c) in bs): # up
        nextarrows.extend([(r-1, c, 0)])
    elif (d == 1 and (r,c) in bs) or (d == 3 and (r,c) in fs): # down
        nextarrows.extend([(r+1, c, 2)])
    else:
        r1 = r
        c1 = c
        d1 = d
        if d == 0:
            r1 = r-1
        elif d == 1:
            c1 = c+1
        elif d == 2:
            r1 = r+1
        elif d == 3:
            c1 = c-1
        nextarrows.extend([(r1, c1, d1)])
    return([x for x in nextarrows if infield(x)])

def run(arrows):
    en = set()
    rays = set()
    while len(arrows) > 0:
        a = arrows.pop(0)
        en.add((a[0], a[1]))
        if a not in rays:
            rays.add(a)
            arrows.extend(step(a))
    return(en)

print('Day 16, part 1:', len(run([(0,0,1)])))

top = [(0,c,2) for c in range(cmax)]
bot = [(rmax-1, c, 0) for c in range(cmax)]
lef = [(r, 0, 1) for r in range(rmax)]
rig = [(r, cmax-1, 3) for r in range(rmax)]
start = top + bot + lef + rig

ans = 0
for st in start:
    en = run([st])
    ans = max(len(en), ans)

print('Day 16, part 2:', ans)
