data= ["Time:        54     70     82     75", "Distance:   239   1142   1295   1253" ]
 #data = ["Time:      7  15   30", "Distance:  9  40  200"] # Test data
 
 # Part 1
def dist(time):
    d =[]
    for x in range(0,time+1):
        d.append(time*x - x*x)
    return(d)
 
boats = []
for i in range(1, len(data[0].split())):
    boats.append((int(data[0].split()[i]), int(data[1].split()[i])))
 
ans = 1  
for b in boats:
    t,d = b
    this = len([x for x in dist(t) if x > d])
    if this > 0:
        ans = ans * this
   
print('Day 6, part 1:', ans)
 
# Part 2
boat = (int(''.join(data[0].split()[1:])), int(''.join(data[1].split()[1:])))
 
def func(a, x):
    return(a*x - x*x)

# OK, brute force, whatever.
for x in range(0, boat[0]):
    y = func(boat[0], x)
    if y > boat[1]:
        print('Day 6, part 2:', boat[0] - 2 * x + 1)
        exit()