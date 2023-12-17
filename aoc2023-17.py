import heapq
data = [x.strip() for x in open('aoc2023-17-input.txt')]

maze = {}
start = (0,0)
for r, row in enumerate(data):
    for c, ch in enumerate(row):
        maze[(r,c)] = int(ch)
goal = (r,c)

def inside(p): # (r, c)
    global start, goal
    return(all([start[0] <= p[0] <= goal[0], start[1] <= p[1] <= goal[1]]))

def step(fr, d):
    return(fr[0] + d[0], fr[1] + d[1])

# In the Q, have [(heat, (r, c), (dr, dc), st)]
# st is number of steps in the same direction.

def solve(part2 = False):
    Q = []
    heapq.heappush(Q, (0, start, (0,1), 0))
    heapq.heappush(Q, (0, start, (1,0), 0))
    heatmap = {} # For storing lowest heats at different points.
    while Q:
        
        h, p, d, s = heapq.heappop(Q) # p = point, d = direction, s = steps straight to point, h = heat including point
        if p == goal:
            return(h)

        if (p, d, s) not in heatmap.keys() or h < heatmap[(p, d, s)]:
            heatmap[(p, d, s)] = h
            p2 = step(p, d) # Take a look at p2.
            s2 = s + 1 # One more step straight to go to p2.
            if inside(p2) and ((part2 and s2 <= 10) or s2 <= 3):
 
                h2 = h + maze[(p2)]

                heapq.heappush(Q, (h2, p2, d, s2)) # Continue in the same direction.
                if not part2 or (part2 and s2 >= 4):
                    d2a = d[1], d[0]
                    d2b = -d[1], -d[0]
                    heapq.heappush(Q, (h2, p2, d2a, 0)) # Other direction 2a.
                    heapq.heappush(Q, (h2, p2, d2b, 0)) # Other direction 2b.

print('Day 17, part 1:', solve())

print('Day 17, part 2:', solve(True))