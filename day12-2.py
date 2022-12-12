import sys, tools
rows = 0
inp = []
for l in sys.stdin:
    rows += 1
    inp += [l[:-1]]

cols = 0
for s in inp[0]:
    cols += 1

grid = [[{"h": 0, "up": 0, "dist": 9999999} for _ in tools.norng(cols)] for __ in tools.norng(rows)]

start = []
finish = []

targs = []

for i in tools.rng(rows):
    for j in tools.rng(cols):
        grid[i][j]["pos"] = [i,j]
        grid[i][j]["up"] = ord(inp[i][j]) - 96
        if inp[i][j] == "S" or inp[i][j] == "a":
            targs += [grid[i][j]]
            grid[i][j]["up"] = 1
            grid[i][j]["dist"] = 0
        if ord(inp[i][j]) == 69:
            finish = [i,j]
            grid[i][j]["up"] = 26

nbors = lambda x,y: [val for val in [[x-1, y],[x, y-1], [x+1, y], [x, y+1]] if val[0] != -1 and val[1] != -1 and val[0] != rows and val[1] != cols]

for i in tools.rng(rows):
    for j in tools.rng(cols):
        grid[i][j]["h"] = abs(i - finish[0]) + abs(j - finish[1])
        grid[i][j]["nbors"] = [[x,y] for [x,y] in nbors(i,j) if grid[x][y]["up"] <= grid[i][j]["up"] + 1]

for _ in tools.norng(100000000):
    targs_min = targs[0]["dist"] + targs[0]["h"]
    targ_top = targs[0]
    for targ in targs[1:]:
        if targ["dist"] + targ["h"] < targs_min:
            targ_top = targ
    targs = [x for x in targs if x != targ_top]
    nxt = targ_top
    if nxt == grid[finish[0]][finish[1]]:
        print("so cool!")
        print(nxt["dist"])
    for [x,y] in nxt["nbors"]:
        if grid[x][y]["dist"] > nxt["dist"] + 1:
            grid[x][y]["dist"] = nxt["dist"] + 1
            targs += [grid[x][y]]

print(start)
print(finish)