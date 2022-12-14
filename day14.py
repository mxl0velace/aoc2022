import sys, tools
inp = []
for l in sys.stdin:
    inp += [l[:-1].split(" -> ")]

fl = 500
fr = 500
fb = 0


for l in inp:
    for v in tools.rng(tools.ln(l)):
        l[v] = list(map(int,l[v].split(",")))
        if l[v][0] < fl:
            fl = l[v][0]
        if l[v][0] > fr:
            fr = l[v][0]
        if l[v][1] > fb:
            fb = l[v][1]

grid = []

for l in inp:
    for v in tools.rng(tools.ln(l) - 1):
        s = l[v]
        f = l[v+1]
        if s[0] == f[0]:
            if s[1] > f[1]:
                for off in tools.rng(s[1] - f[1] + 1):
                    grid += [[s[0], f[1] + off]]
            if s[1] < f[1]:
                for off in tools.rng(f[1] - s[1] + 1):
                    grid += [[s[0], s[1] + off]]
        if s[1] == f[1]:
            if s[0] > f[0]:
                for off in tools.rng(s[0] - f[0] + 1):
                    grid += [[f[0] + off, f[1]]]
            if s[0] < f[0]:
                for off in tools.rng(f[0] - s[0] + 1):
                    grid += [[s[0] + off, s[1]]]

fl -= 1
fr += 1

x = 0

print("Sim-ing")

for __ in tools.norng(100000):
    pos = [500,0]
    for _ in tools.norng(fb + 1):
        mvd = 0
        mvl = 0
        mvr = 0

        if not [pos[0],pos[1]+1] in grid:
            mvd = 1
        if not [pos[0]-1,pos[1]+1] in grid:
            mvl = 1
        if not [pos[0]+1,pos[1]+1] in grid:
            mvr = 1
        
        if mvd == 1:
            pos = [pos[0],pos[1]+1]
        if mvd == 0 and mvl == 1:
            pos = [pos[0]-1,pos[1]+1]
        if mvd == 0 and mvl == 0 and mvr == 1:
            pos = [pos[0]+1,pos[1]+1]
    print(f"Calc'd {x}: {pos[1]} : {fb}")
    if pos[1] > fb:
        print(f"Finish at {x}")
        b = 1 / 0
    if pos[1] <= fb:
        grid += [pos]
    x += 1