data = [x.strip() for x in open('aoc2023-05-input.txt') if len(x.strip()) > 0]

# Translate input "ins" according to "table"
def translate(ins, table):
    for item in table:
        dstart, dstop, sstart, sstop = item
        if sstart <= ins <= sstop:
            diff = sstop - ins
            return(dstop - diff)
    return(ins)

# Take one value one step backward through table.
def onebackwards(ins, table):
    for item in table:
        dstart, dstop, sstart, sstop = item
        if dstart <= ins <= dstop:
            diff = dstop - ins
            return(sstop - diff)
    return(ins)

# Run one value backwards through all the tables in megatable.
def backwards(ex, megatable):
    i = len(megatable) - 1
    while i > -1:
        table = megatable[i]
        ex = onebackwards(ex, table)
        i -= 1
    return(ex)

def checkseed(nbr, sds):
    i = 0
    while i < len(sds) - 1:
        start, rng = sds[i], sds[i+1]
        stop = start + rng
        if start <= nbr <= stop:
            return(True)
        i += 2


spec = {}
seeds = []
seeds2 = []
megatable = []

i = 0
while i < len(data):
    line = data[i]

    if line.startswith('seeds'):
        seeds = [int(x) for x in line.split()[1:]]
        i += 1
        j = 0
        while j < len(seeds)-1:
            sstart, slen = seeds[j:j+2]
            j += 1

    elif '-' in line:
        i += 1
        table = []
        while i < len(data) and '-' not in data[i] and len(data[i]) > 0:
            dest, source, nbr = [int(x) for x in data[i].split()]
            table.append((dest, dest+nbr, source, source+nbr))
            i += 1
        megatable.append(table)

        for sn, s in enumerate(seeds):
            seeds2.append(translate(s, table))

    else:
        i += 1

print('Day 5, part 1:', min(seeds2))

apa = 0
while True:
    if apa % 100000 == 0:
        print(apa) # To see the progress.
    testing = backwards(apa, megatable)
    if checkseed(testing, seeds): # A valid seed!
        #print(apa, 'from', testing)
        print('Day 5, part 2:', apa)
        exit()
    apa += 1
