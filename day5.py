import sys
xrng = lambda nx, y: [nx, y != 1 and xrng(nx, y-1) + [y-1]][y != 1]
rng = lambda y: xrng([0], y)

# txt input
inp = []
inst = []
slc = 0
for l in sys.stdin:
    if l == "\n":
        slc = 1
    if slc:
        inst += [l[:-1]]
    if not slc:
        inp += [l[:-1]]

inst = inst[1:]
cols = inp[-1]
inp = inp[:-1]

# format input
box = []
c = 0
for x in cols:
    if x != " ":
        box += [[]]        
        for row in inp:
            if row[c] != " ":
                box[int(x)-1] += [row[c]]
        box[int(x)-1] = box[int(x)-1][::-1]
    c += 1

ninst = []
for l in inst:
    l = l[5:]
    l = l.split(" from ")
    l[1] = l[1].split(" to ")
    ninst += [[int(l[0]), int(l[1][0]), int(l[1][1])]]

box2 = []
for col in box:
    box2 += [col.copy()]

# do our task
for inst in ninst:
    amount = inst[0]
    start = inst[1] - 1
    finish = inst[2] - 1
    c = 0

    for n in rng(amount):
        val = box[start].pop()
        box[finish] += [val]
    
    tograb = box2[start][-amount:]
    box2[start] = box2[start][:-amount]
    box2[finish] += tograb

# show final product
total = ""
for col in box:
    total += col[-1]

print(total)

total_2 = ""
for col in box2:
    total_2 += col[-1]

print(total_2)