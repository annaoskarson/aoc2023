data = [x.strip() for x in open('aoc2023-19-input.txt')]

wf, pl = data[:data.index('')], data[data.index('')+1:]

flows = {}
for w in wf:
    name = w.split('{')[0]
    flows[name] = []
    for r in w.split('{')[1][:-1].split(','):
        if '<' in r or '>' in r:
            item, (val, reg) = r[0], r[2:].split(':')
            sign = r[1]
            val = int(val)
            flows[name].append([item, sign, val, reg])
        else:
            reg = r
            flows[name].append([reg])

parts = []
for p in pl:
    part = {}
    for c in p[1:-1].split(','):
        part[c.split('=')[0]] = int(c.split('=')[1])
    parts.append(part)


def accepted(p, place):
    while place not in ['A', 'R']:
        for rule in flows[place]:
            if len(rule) > 1:
                if rule[1] == '<' and p[rule[0]] < rule[2]:
                    place = rule[-1]
                    break
                elif rule[1] == '>' and p[rule[0]] > rule[2]:
                    place = rule[-1]
                    break
            else:
                place = rule[0]
    if place == 'A':
        return(True)
    elif place == 'R':
        return(False)

A = []
R = []
for p in parts:
    if accepted(p, 'in'):
        A.append(p)
    else:
        R.append(p)

ans = sum([sum(part.values()) for part in A])

print('Day 19, part 1:', ans)

def split(rs, sign, n):
    lo, hi = rs
    if lo < n < hi:
        if sign == '<':
            acc = (lo, n-1)
            rej = (n, hi)
        elif sign == '>':
            acc = (n+1, hi)
            rej = (lo, n)
    elif n < lo and sign == '<': # all too high
        rej = (lo, hi)
    elif hi < n and sign == '<': # all pass
        acc = (lo, hi)
    elif n < lo and sign == '>': # all pass
        acc = (lo, hi)
    elif hi < n and sign == '<': # all too high
        rej = (lo, hi)
    return(acc, rej)


def splitter(B):
    import copy
    A = [] # Holds the accepted parts

    while B:
        place, p = B.pop(0)

        if place == 'A': # p is for keeps!
            A.append(p)
        elif place == 'R': # p is rubbish
            pass
        else: # we don't know yet
            for rule in flows[place]:
                nextplace = rule[-1]
                if len(rule) > 1: # if a limit rule
                    # The copy of p that will pass this rule.
                    p_pass = copy.deepcopy(p)
                    rang = p[rule[0]]
                    sign = rule[1]
                    limit = rule[2]

                    # split the ranges into pass range and fail range.
                    r_pass, r_fail = split(rang, sign, limit)

                    p_pass[rule[0]] = r_pass
                    B.append((nextplace, p_pass))
                    
                    p[rule[0]] = r_fail # pass p on to next rule at the place
                else: # direct path
                    B.append((nextplace, p))

    return(A) # all the passed parts



Mp = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
blobs = [('in', Mp)] # Starting position
A = splitter(blobs)

def evaluate(p):
    r = 1
    for xmas in p.values():
        r *= xmas[1] - xmas[0] + 1
    return(r)

ans = sum([evaluate(p) for p in A])

print('Day 19, part 2:', ans)
