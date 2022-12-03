import sys

inp = []
for l in sys.stdin:
    inp += [l[:-1]]

ording = "abcd"+chr(101)+"fghijklmnopqrstuvwxyzABCD"+chr(69)+"FGHIJKLMNOPQRSTUVWXYZ"

total = 0

for l in inp:
    long = 0
    for x in l:
        long += 1
    additional = l[int(long/2):]
    first = l[:int(long/2)]

    foundval = -1

    for x in additional:
        if x in first:
            rolling = 0
            for y in ording:
                rolling += 1
                if x == y:
                    foundval = rolling
    
    total += foundval

print(total)