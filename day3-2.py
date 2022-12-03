import sys

inp = []
for l in sys.stdin:
    inp += [l[:-1]]

ording = "abcd"+chr(101)+"fghijklmnopqrstuvwxyzABCD"+chr(69)+"FGHIJKLMNOPQRSTUVWXYZ"

total = 0

l1 = inp[::3]
l2 = inp[1::3]
l3 = inp[2::3]

c = 0
for lf1 in l1:
    lf2 = l2[c]
    lf3 = l3[c]
    c += 1
    foundval = -1
    for l in lf1:
        if l in lf2 and l in lf3:
            rolling = 0
            for y in ording:
                rolling += 1
                if l == y:
                    foundval = rolling
    total += foundval 

print(total)