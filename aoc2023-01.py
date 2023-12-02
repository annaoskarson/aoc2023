import re
data = [r.strip('\n') for r in open('aoc2023-01-input.txt')]

def parsenumber(text, both):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    first_pos = len(text)
    last_pos = -1
    for n,c in enumerate(text):
        if c.isdigit(): #The digits
            if n < first_pos:
                first_pos, first = n, int(c)
            if n > last_pos:
                last_pos, last = n, int(c)
        elif both: #The letters
            for pos, digit in enumerate(digits):
                if text[n:].startswith(digit):
                    if n < first_pos:
                        first_pos, first = n, pos+1
                    if n > last_pos:
                        last_pos, last = n, pos+1
    return(first*10 + last)

def partone(data):
    sum = 0    
    for row in data:
        sum = sum + parsenumber(row,False)
    return(sum)

def parttwo(data):
    sum = 0    
    for row in data:
        sum = sum + parsenumber(row,True)
    return(sum)

print('Day 1, part 1:', partone(data))
print('Day 1, part 2:', parttwo(data))