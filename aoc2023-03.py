data = [r.strip('\n') for r in open('aoc2023-03-input.txt')]

themap = set() # positions of all the symbols
digits = [] # list of ( [coords], value ), where coords is the coords of the digits in the value
gears = set() # positions of all the gears

# Make the map and the digits, and the gears.
y = 0
while y < len(data):
    x = 0
    line = data[y]
    while x < len(line):

        # A symbol found.
        if (not line[x].isnumeric()) and (line[x] != '.'):
            themap.add((x,y))
            if line[x] == '*': # A gear found.
                gears.add((x,y))
            x += 1

        # A digit found.
        elif line[x].isnumeric():
            coords = set()
            digit = ''
            # Gather the whole number.
            while x < len(line) and line[x].isnumeric(): 
                coords.add((x,y))
                digit = digit + line[x]
                x += 1
            digits.append((coords, int(digit)))

        else:
            x += 1

    y += 1

# Function to get all the neighbours to p.
def nb(p):
    x,y = p
    nbs = set()
    for y1 in [y-1, y, y+1]:
        for x1 in [x-1, x, x+1]:
            nbs.add((x1,y1))
        #nbs = nbs - set((p)) # Remove the point itself from the neighbour list. Not necessary in this case.
    return(nbs)

# Check, for all digits, if it has a neighbouring symbol.
ans = 0
for points, value in digits:
    dnbs = set() # digitneighbours
    for point in points:
        dnbs.update(nb(point))
    #dnbs = dnbs - points # just to remove the place for the digits, not necessary
    if dnbs & themap: # The digit is neighbouring a symbol in the map.
        ans += value

def adj_2(p): # Check if p has exactly two digit neigbours, and return the product of the two, or zero.
    resultlist = []
    nbs = set(nb(p)) # all neigbours of p

    for points, val in digits: # check for every digit, if it is neigbouring
        if nbs & set(points): # this digit is neigbhour to gear
            resultlist.append(val)
        if len(resultlist) > 2:
            return(0)
    if len(resultlist) == 2:
       return(resultlist[0] * resultlist[1])
    return(0)

sumgear = 0
for g in gears:
    sumgear += adj_2(g)
 
print('Day 3, part 1:', ans)
print('Day 3, part 2:', sumgear)
