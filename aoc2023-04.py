cards = [r.strip('\n') for r in open('aoc2023-04-input.txt')]

ans1 = 0
amount = {} # Holds the amount of each card.

for card in cards:
    n = int(card.split(':')[0].split(' ')[-1])
    hand = set([int(x) for x in card.split(':')[1].split('|')[0].strip().split(' ') if len(x) > 0])
    win = set([int(x) for x in card.split(':')[1].split('|')[1].strip().split(' ') if len(x) > 0])

    points = len(hand & win)

    # Look at this card and add it to the stash.
    if n not in amount.keys():
        amount[n] = 1
    else:
        amount[n] += 1
 
    have = amount[n] #The amount we have of this card.

    if points > 0: # If we win, do the thing
        # For part 1, count the points.
        ans1 = ans1 + (2**(points - 1 ))

        # For part 2, add more scratchcards in the stash, 
        # the amount for each card ahead is defined from how many we have of the current card.
        for i in range(n+1, n+1+points):
            if i not in amount.keys():
                amount[i] = have
            else:
                amount[i] += have


ans2 = 0
for this in amount.keys():
    ans2 = ans2 + amount[this]

print('Day 4, part 1:', ans1)
print('Day 4, part 2:', ans2)
