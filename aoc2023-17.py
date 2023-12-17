data = [x.strip() for x in open('aoc2023-17-input.txt')]

maze = {}
start = (0,0)
for r, row in enumerate(data):
    for c, ch in enumerate(row):
        maze[(r,c)] = int(ch)
goal = (r,c)

def inside(p): # r, c
    global start, goal
    return(all([start[0] <= p[0] <= goal[0], start[1] <= p[1] <= goal[1]]))

def step(fr, d):
    return(fr[0] + d[0], fr[1] + d[1])

# In the Q, have [((r, c), (dr, dc), st, heat)]
# st is number of steps in the same direction.

def solve(Q, part2 = False):
    global heatmap
    while Q:

        Q.sort(key=lambda tup: tup[3])
        
        p, d, s, h = Q.pop(0) # p = point, d = direction, s = steps straight to point, h = heat including point
        if p == goal:
            print()
            return(h)

        if (p, d, s) not in heatmap.keys() or h < heatmap[(p, d, s)]:
            heatmap[(p, d, s)] = h
            p2 = step(p, d) # Take a look at p2.
            s2 = s + 1 # One more step straight to go to p2.
            if inside(p2) and ((part2 and s2 <= 10) or s2 <= 3):
 
                h2 = h + maze[(p2)]

                Q.append((p2, d, s2, h2)) # Continue in the same direction.
                # directions: d2a = dc, dr and d2b = -dc, -dr
                if not part2 or (part2 and s2 >= 4):
                    d2a = d[1], d[0]
                    d2b = -d[1], -d[0]
                    Q.append((p2, d2a, 0, h2)) # Other direction 2a.
                    Q.append((p2, d2b, 0, h2)) # Other direction 2b.

p = [(start, (0,1), 0, 0), (start, (1,0), 0, 0)]
heatmap = {} # For storing lowest heats at different points.
print('Day 17, part 1:', solve(p))

p = [(start, (0,1), 0, 0), (start, (1,0), 0, 0)]
print('Day 17, part 2:', solve(p, True))

# This takes ages ... But it works. Should try with a sorted stack of some kind.