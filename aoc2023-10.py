import collections
#maze = [x.strip() for x in open('aoc2023-10-input.txt')]
# Changed to lists. Maybe change back to see if that is faster.
maze = [list(x.strip()) for x in open('aoc2023-10-input.txt')]

def go(this, last, maze):
    this_tile = maze[this[0]][this[1]]
    row, col = this
    # Find the two alternative positions to go to.
    if this_tile == '|':
        alt = [(row+1, col), (row-1, col)]
    elif this_tile == '-':
        alt = [(row, col+1), (row, col-1)]
    elif this_tile == 'L':
        alt = [(row-1, col), (row, col+1)]
    elif this_tile == 'J':
        alt = [(row-1, col), (row, col-1)]
    elif this_tile == '7':
        alt = [(row, col-1), (row+1, col)]
    elif this_tile == 'F':
        alt = [(row+1, col), (row, col+1)]
    alt.remove(last) # Remove where we came from.
    return(alt[0]) # Return the next point.

def startpoint(maze):
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == 'S':
                return((r,c))

def starting(this, maze):
    (row, col) = this
    if maze[row-1][col] in ['|', 'F', '7']:
        return((row-1, col))
    elif maze[row][col+1] in ['-', 'J', '7']:
        return((row, col+1))
    elif maze[row+1][col] in ['|', 'J', 'L']:
        return((row+1, col))
    elif maze[row][col-1] in ['-', 'F', 'L']:
        return((row, col-1))

way = []
n0 = startpoint(maze)
n1 = starting(startpoint(maze), maze)
way.append(n0)
way.append(n1)
while maze[way[-1][0]][way[-1][1]] != 'S':
    nx = go(way[-1], way[-2], maze)
    way.append(nx)

print('Day 10, part 1:', (len(set(way)))//2)

# Change the S to whatever it should be ...
# Let's hope that it works, haven't tested all cases.
nl = way[-2]
if n1[0] == nl[0]: # same row
    ch = '-'
elif n1[1] == nl[1]: # same col
    ch = '|'
elif (n0[0] < n1[0] and n0[1] < nl[1]) or (n0[0] < nl[0] and n0[1] < n1[1]):
    ch = 'F'
elif (n0[0] < n1[0] and n0[1] > nl[1]) or (n0[0] < nl[0] and n0[1] > n1[1]):
    ch = 'L'
elif (n0[0] > n1[0] and n0[1] > nl[1]) or (n0[0] > nl[0] and n0[1] > n1[1]):
    ch = '7'
elif (n0[0] > n1[0] and n0[1] < nl[1]) or (n0[0] > nl[0] and n0[1] < n1[1]):
    ch = 'J'
maze[n0[0]][n0[1]] = ch

# Prettyprint, way is coordinates for the loop, inside is the trapped tiles.
def pprint(maze, way = [], inside = []):
    for r, row in enumerate(maze):
        newrow = ''
        for c, ch in enumerate(row):
            if (r,c) in inside:
                newrow = newrow + '█'
            elif len(way) == 0 or (r,c) in way:
                newrow = newrow + ch
            else:
                newrow = newrow + '.'
        print(newrow)

# Inside if odd number of walls in any direction?
def inside(point, maze, way):
    row, col = point
    if row in [0, len(maze)] or col in [0, len(maze[0])]:
        # On the edge, cannot be inside.
        return(False)
    # Just look in one direction. If there is an odd number of blockers,
    # we are inside. I decide to look west.
    d = [maze[row][c] for c in range(0, col) if (row, c) in way]
    if len(d) == 0 or all(x == '.' for x in d):
        return(False)
    else:
        r = collections.Counter(d)
        block = r['|']
        if r['F'] > 0:
            block += min(r['F'], r['J'])
        if r['7'] > 0:
            block += min(r['7'], r['L'])
        if block % 2 != 0:
            return(True)
        else:
            return(False)

trapped = []
test = set([(r,c) for r in range(len(maze)-1) for c in range(len(maze[0])-1)]) - set(way)
for r,c in test:
    if inside((r,c), maze, way):
        trapped.append((r,c))

#pprint(maze, way)
#print()
#pprint(maze, way, trapped)

print('Day 10, part 2:', len(set(trapped)))