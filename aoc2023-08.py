import math
data = [x.strip() for x in open('aoc2023-08-input.txt')]

ins = data[0].replace('L', '0').replace('R', '1')
themap = {}
for node in data[2:]:
    themap[node.split()[0]] = (node.split()[2][1:-1], node[-4: -1])

def run(start, stop, ins, themap):
    this = start
    i = 0
    while not(this in stop):
        this = themap[this][int(ins[i % len(ins)])]
        i += 1
    #print(start, this) shows that each start has a uniqe stop.
    return(i)

print('Day 8, part 1:', run('AAA', ['ZZZ'], ins, themap))

startfield = [x for x in themap.keys() if x.endswith('A')]
endings = [x for x in themap.keys() if x.endswith('Z')]

points = []
for x in startfield:
    points.append(run(x, endings, ins, themap))

# Tried the lcm method, and it worked. Otherwise, had to check
# if two starts share loop or something ... If that is even possible.
# Or if they start mid-loop or something.
print('Day 8, part 2:', math.lcm(*points))