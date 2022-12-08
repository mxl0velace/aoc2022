import sys, tools

inp = []
grid = []
inp_l = 0
inp_r_l = 0

# load data
for l in sys.stdin:
    grid += [[]]
    inp += [list(map(int,list(l[:-1])))]
    inp_r_l = 0
    for x in l[:-1]:
        inp_r_l += 1
        grid[inp_l] += [0]
    inp_l += 1

# part 1
for r in tools.rng(inp_l):
    vis_l = -1
    for c in tools.rng(inp_r_l):
        if inp[r][c] > vis_l:
            grid[r][c] = 1
            vis_l = inp[r][c]
    
    vis_l = -1
    for c in tools.rng(inp_r_l):
        if inp[r][-(c+1)] > vis_l:
            grid[r][-(c+1)] = 1
            vis_l = inp[r][-(c+1)]

for r in tools.rng(inp_r_l):
    vis_l = -1
    for c in tools.rng(inp_l):
        if inp[c][r] > vis_l:
            grid[c][r] = 1
            vis_l = inp[c][r]
    
    vis_l = -1
    for c in tools.rng(inp_l):
        if inp[-(c+1)][r] > vis_l:
            grid[-(c+1)][r] = 1
            vis_l = inp[-(c+1)][r]

total = sum(map(sum,grid))
print(total)

# part 2
total_2 = 0
for r in tools.rng(inp_l):
    for c in tools.rng(inp_r_l):
        up = 0
        down = 0
        lft = 0
        right = 0

        if c != 0:
            vis = 0
            if c == 1:
                lft = 1
            if c != 1:
                for o_r in tools.rng(c):
                    if vis == 0 and inp[r][c-(o_r+1)] >= inp[r][c]:
                        vis = 1
                        lft += 1
                    if vis == 0 and inp[r][c-(o_r+1)] < inp[r][c]:
                        lft += 1
        
        if c != inp_r_l - 1:
            vis = 0
            if c == inp_r_l - 2:
                right = 1
            if c != inp_r_l - 2:
                for o_r in tools.rng(inp_r_l - 1 - c):
                    if vis == 0 and inp[r][c+(o_r+1)] >= inp[r][c]:
                        vis = 1
                        right += 1
                    if vis == 0 and inp[r][c+(o_r+1)] < inp[r][c]:
                        right += 1
        
        if r != 0:
            vis = 0
            if r == 1:
                up = 1
            if r != 1:
                for o_r in tools.rng(r):
                    if vis == 0 and inp[r-(o_r+1)][c] >= inp[r][c]:
                        vis = 1
                        up += 1
                    if vis == 0 and inp[r-(o_r+1)][c] < inp[r][c]:
                        up += 1
        
        if r != inp_l - 1:
            vis = 0
            if r == inp_l - 2:
                down = 1
            if r != inp_l - 2:
                for o_r in tools.rng(inp_l - 1 - r):
                    if vis == 0 and inp[r+(o_r+1)][c] >= inp[r][c]:
                        vis = 1
                        down += 1
                    if vis == 0 and inp[r+(o_r+1)][c] < inp[r][c]:
                        down += 1
            
        tr = up * down * lft * right
        if tr > total_2:
            total_2 = tr

print(total_2)