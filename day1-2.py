import sys

inp = ""
for l in sys.stdin:
    inp += l 

totals = []

for l in inp.split("\n\n"):
    thiscount = 0
    for x in l.split("\n"):
        if x != '':
            thiscount += int(x)
    totals += [thiscount]

totals.sort()
print(totals[-1] + totals[-2] + totals[-3])