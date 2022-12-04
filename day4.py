import sys

inp = []
for l in sys.stdin:
    inp += [l[:-1]]

total = 0

total_2 = 0

for l in inp:
    pairs = l.split(",")
    p1 = pairs[0].split("-")
    p2 = pairs[1].split("-")
    f = 0
    if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1]):
        total += 1
        total_2 += 1
        f = 1
    if int(p2[0]) <= int(p1[0]) and int(p2[1]) >= int(p1[1]) and f == 0:
        total += 1
        total_2 += 1
        f = 1
    if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[0]) and f == 0:
        total_2 += 1
        f = 1
    if int(p1[0]) >= int(p2[0]) and int(p1[0]) <= int(p2[1]) and f == 0:
        total_2 += 1

print(total)
print(total_2)