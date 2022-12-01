import sys

inp = ""
for l in sys.stdin:
    inp += l 

top = 0

for l in inp.split("\n\n"):
    thiscount = 0
    for x in l.split("\n"):
        if x != '':
            thiscount += int(x)
    if thiscount > top:
        top = thiscount

print(top)