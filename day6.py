import sys

#txt input
inp = ""
for x in sys.stdin:
    inp = x[:-1]

found = 0
found_2 = 0
l = 3

for c in inp:
    l += 1
    sc = inp[l-4:l]
    sc2 = inp[l-4:l+10]
    if found == 0 and sc.count(sc[0]) == 1 and sc.count(sc[1]) == 1 and sc.count(sc[2]) == 1 and sc.count(sc[3]) == 1:
        print(f"Found at {l}")
        found = 1
    
    if found_2 == 0 and all(map(lambda x: sc2.count(x) == 1, sc2)):
        print(f"Found part 2 at {l+10}")
        found_2 = 1