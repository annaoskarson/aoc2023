import collections
cards = [r.strip('\n') for r in open('aoc2023-04-input.txt')]

ans1 = 0
amount = collections.Counter() # Holds the amount of each card.

for card in cards:
    n = int(card.split(':')[0].split(' ')[-1])
    hand = set([int(x) for x in card.split(':')[1].split('|')[0].strip().split()])
    win = set([int(x) for x in card.split(':')[1].split('|')[1].strip().split()])

    points = len(hand & win)

    amount[n] += 1 # Look at this card and add it to the stash.   
    have = amount[n] # The amount we have of this card.

    if points > 0: # If we win, do the thing
        # For part 1, count the points.
        ans1 = ans1 + (2**(points - 1 ))

        # For part 2, add more scratchcards in the stash, 
        # the amount for each card ahead is defined from how many we have of the current card.
        for i in range(n+1, n+1+points):
            amount[i] += have

ans2 = amount.total()

print('Day 4, part 1:', ans1)
print('Day 4, part 2:', ans2)
