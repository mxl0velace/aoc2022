import sys, tools

inp = []
for l in sys.stdin:
    inp += l[:-1].split(" ")

c = 0
x = 1
total = 0
grid = []

for l in inp:
    pos = c%40
    grid += [0]
    if x == pos or x == pos+1 or x == pos-1:
        grid[c-1] = 1

    c += 1
    if c in [20,60,100,140,180,220]:
        total += x * c

    if l != "noop" and l !="addx":
        x += int(l)

print(total)

c = 0
lin = ""
for sy in grid:
    c += 1
    if c%40 == 0:
        print(lin)
        lin = ""
    if sy == 0:
        lin += ". "
    if sy == 1:
        lin += "# "
