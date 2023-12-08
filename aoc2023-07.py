import collections

hands = [(x.strip().split()[0], int(x.strip().split()[1])) for x in open('aoc2023-07-input.txt')]

types = ['fives', 'fours', 'house', 'threes', 'twopair', 'onepair', 'highcard']

def whatis(c): # Rewritten, works for both parts.
    jokers = 5 - len(c)
    if all(x == c[0] for x in c) or len(c) == 0:
        return(types[0])
    elif collections.Counter(c).most_common()[0][1] + jokers == 4:
        return(types[1]) 
    elif  collections.Counter(c).most_common()[0][1] + jokers == 3 and collections.Counter(c).most_common()[1][1] == 2:
        return(types[2]) # AAJ55, AAAJJ
    elif collections.Counter(c).most_common()[0][1] + jokers == 3:
        return(types[3]) # AAJ23 AJJ23
    elif collections.Counter(c).most_common()[0][1] + jokers == 2 and collections.Counter(c).most_common()[1][1] == 2:
        return(types[4]) # AA223 No room for J here?
    elif len(c) == 4 or collections.Counter(c).most_common()[0][1] + jokers == 2:
        return(types[5]) # J2345
    elif len(set(c)) == len(c):
        return(types[6])       

def best(t1, t2, part2=False):
    t1c, _ = t1
    t2c, _ = t2
    complist = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if part2:
        complist = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    i = 0
    while i < len(t1c):
        if complist.index(t1c[i]) < complist.index(t2c[i]):
            return(t1)
        elif complist.index(t1c[i]) > complist.index(t2c[i]):
            return(t2)
        i += 1

def insert(item, thelist, part2 = False):
    i = 0
    while i < len(thelist):
        if best(item, thelist[i], part2) == item:
            return(thelist[:i] + [item] + thelist[i:])
        i += 1
    return(thelist + [item])

def bestoption(thelist):
    has = []
    for cards in thelist:
        t = whatis(cards)
        has.append(t)
    for ty in types:
        if ty in has:
            return(ty)

# Select which part to run.
part2 = False

def bucketsort(hands):
    buckets = {}
    buckets2 = {}
    for kind in types:
        buckets[kind] = []
        buckets2[kind] = []
    for hand in hands:
        cards, points = hand
        # Part 2
        if 'J' in cards:
            # Turns out that the best option is to add the J:s to the most common card in hand.
            # Removing J:s work with my bucket sorting.
            thebest = whatis([x for x in cards if x != 'J'])
            buckets2[thebest].append(hand)
        else:
            buckets2[whatis(cards)].append(hand)
        buckets[whatis(cards)].append(hand)
    return(buckets, buckets2)

def sortbuckets(buckets, part2 = False):
    sortedlist = []
    for bucket in types:
        if len(buckets[bucket]) == 1:
            sortedlist.extend(buckets[bucket])
        else:
            templist = buckets[bucket][:1]
            for this in buckets[bucket][1:]:
                templist = insert(this, templist, part2)

            sortedlist.extend(templist)
    return(sortedlist)

def ranking(list):
    ans = 0
    rank = len(list)
    i = 0
    while i < len(list):
        ans += rank * list[i][1]
        i += 1
        rank -= 1
    return(ans)

part1, part2 = bucketsort(hands)
part1sorted = sortbuckets(part1)
part2sorted = sortbuckets(part2, True) # Boolean to get the right sorting method.

print('Day 7, part 1:', ranking(part1sorted))
print('Day 7, part 2:', ranking(part2sorted))

