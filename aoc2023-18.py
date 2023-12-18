code = [x.strip() for x in open('aoc2023-18-input.txt')]

def pprint(ls):
    rmin, rmax, cmin, cmax = borders(ls)
    for r in range(rmin, rmax+1):
        row = ''
        for c in range(cmin, cmax+1):
            if (r,c) not in ls:
                row += '#'
            else:
                row += '.'
        print(row)
    print()

def borders(ls):
    rmin = min(ls, key = lambda t: t[0])[0] - 1
    rmax = max(ls, key = lambda t: t[0])[0] + 1
    cmin = min(ls, key = lambda t: t[1])[1] - 1
    cmax = max(ls, key = lambda t: t[1])[1] + 1
    return(rmin, rmax, cmin, cmax)

def cubmeters(soil):
    rmin, rmax, cmin, cmax = borders(soil)
    Q = [(rmin, cmin)]

    def nbs(r,c):
        n = [(rn, cn) for rn in [r-1, r, r+1] for cn in [c-1, c, c+1]]
        n = [(rn, cn) for (rn, cn) in n if (rmin <= rn <= rmax) and (cmin <= cn <= cmax) and (rn, cn) != (r, c)]
        return(n)

    undug = set()
    undug.add(Q[0])
    while Q:
        (r1,c1) = Q.pop(0)
        ns = [(r,c) for (r,c) in nbs(r1, c1) if not((r,c) in soil) and not((r,c) in undug)]
        for (r2, c2) in ns:
            undug.add((r2,c2))
        Q.extend(ns)
    return(undug)

dug = {}
dug[(0,0)] = '#000000'
this = (0,0)
dirs = {'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)}
for row in code:
    d, n, c = row.split()[0], int(row.split()[1]), row.split()[2][1:-1]
    for _ in range(n):
        this = (this[0] + dirs[d][0], this[1] + dirs[d][1])
        dug[this] = c

undug = cubmeters(set(dug.keys()))
rmin, rmax, cmin, cmax = borders(dug.keys())
ans = 0
ans = (rmax-rmin+1)*(cmax-cmin+1) - len(undug)
#pprint(set(undug))
print('Day 18, part 1:', ans)

# Här börjar del 2.
this = (0,0)
ex = []
ex.append(this)
ditch = 0
for row in code:
    dist = int(row.split()[2][1:-1][1:][:-1], 16)
    w = int(row.split()[2][1:-1][1:][-1:])
    # 0 means R, 1 means D, 2 means L, and 3 means U
    d = [(0,1), (1,0), (0,-1), (-1,0)][w]
    ditch += (dist + 1)
    this = (this[0] + d[0]*dist, this[1] + d[1]*dist)
    ex.append(this)

# Så, jag tog ett jävla paket.
from shapely.geometry import Polygon
polygon = Polygon(ex)
# Men sen räckte ju inte det, utan jag fick fixa med lite siffermagi också.
# Polygonarean, plus halva diket, minus häldften antal svängar, plus ett komma fem. Heh.
print('Day 18, part 2:', int(polygon.area + ditch/2 + 1 - len(ex)/2 + 0.5))

#Såhär kan man också göra, har jag surfat fram ...
def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

print('               ', int(area(ex) + ditch/2 +1 - len(ex)/2 + 0.5))