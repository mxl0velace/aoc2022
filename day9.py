import sys, tools

inp = []
for l in sys.stdin:
    inp += [l.split(" ")]

pos_h = [0,0]
pos_t = [0,0]

dirs = {
    "U": [0,1],
    "D": [0,-1],
    "L": [-1,0],
    "R": [1,0]
}

pos_c = {str([0,0]): 1}

for l in inp:
    for st in tools.rng(int(l[1])):
        pos_h = [sum(x) for x in zip(pos_h, dirs[l[0]])]
        pos_diff = [p_h - p_t for p_h, p_t in zip(pos_h, pos_t)]
        if pos_diff[0] > 1 or pos_diff[0] < -1 or pos_diff[1] > 1 or pos_diff[1] < -1:
            if pos_diff[0] > 1:
                pos_diff[0] = 1
            if pos_diff[0] < -1:
                pos_diff[0] = -1
            if pos_diff[1] > 1:
                pos_diff[1] = 1
            if pos_diff[1] < -1:
                pos_diff[1] = -1
            
            pos_t = [sum(x) for x in zip(pos_t, pos_diff)]
            pos_c[str(pos_t)] = 1

total = 0
for v in pos_c:
    total += 1

print(total)