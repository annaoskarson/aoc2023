data = [x for x in open('aoc2023-15-input.txt')][0]
#data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

steps = data.split(',')

def calc(text):
    val = 0
    i = 0
    while i < len(text):
        ch = step[i]
        val += ord(ch)
        val = (val * 17) % 256
        i += 1
    return(val)

ans = []
for step in steps:
    ans.append(calc(step))

print('Day 15, part 1:', sum(ans))

def update(box, label, value):
    for x, (l, v) in enumerate(box):
        if l == label: # Update value
            box[x] = (label, int(value))
            return(box)
    box.append((label, int(value))) # Otherwise, add in box
    return(box)

import collections
boxes = collections.defaultdict(list)

for i, step in enumerate(steps):
    if '=' in step:
        label, value = step.split('=')
        b = calc(label)
        boxes[b] = update(boxes[b], label, value)

    elif '-' in step:
        label = step[:-1]
        b = calc(label)
        boxes[b] = [(l, v) for l, v in boxes[b] if l != label]

power = []
for box in boxes.keys():
    b = box + 1
    for l, lens in enumerate(boxes[box]):
        l = l + 1
        v = lens[1]
        power.append(b*l*v)

print('Day 15, part 2:', sum(power))
