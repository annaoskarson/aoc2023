data = [x.strip() for x in open('aoc2023-12-input.txt')]

lookup = {} # For saving already calculated ends.

def solve(springs, groups):
    global lookup
    times = 0

    K = (springs, tuple(groups))
    if K in lookup.keys(): # Then we can take a shortcut here.
        return(lookup[K])

    if len(groups) == 0 and '#' not in springs: # Done.
        return(1)
    elif len(groups) == 0: # It is '#' left that we did not match.
        return(0)
    elif len(springs) < (sum(groups) + len(groups) - 1): # Not enough left to try.
        return(0)
    elif '.' not in springs[:groups[0]] and ((groups[0] == len(springs)) or (springs[groups[0]] not in ['#'])):
        times += solve(springs[groups[0] + 1:], groups[1:])

    if springs[0] != '#': # If next one is not a '#' we can try skipping that.
        times += solve(springs[1:], groups)

    lookup[K] = times
    return(times)
        
ans = []
for row in data:
    s, g = row.split()[0], [int(x) for x in row.split()[1].split(',')]
    ans.append(solve(s, g))

print('Day 12, part 1:', sum(ans))

ans = []
for r, row in enumerate(data):
    s, g = row.split()[0], [int(x) for x in row.split()[1].split(',')]
    ms = 4*(s+'?') + s
    mg = 5*g
    ans.append(solve(ms,mg))
print('Day 12, part 2:', sum(ans))
