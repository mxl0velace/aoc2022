import sys, tools

inp = []
for l in sys.stdin:
    inp += [l[:-1]]

dirup = {}
dircont = {}
dirsiz = {}
dirall = {}
dirtru = {}

location = "/"
dirall[location] = 1
for l in inp:
    l = l.split(" ")
    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "/":
                location = ""
            if l[2] == "..":
                location = location[:location.rfind("/")]
                if location == "":
                    location = "/"
            if l[2] not in ["/", ".."]:
                if location != "/":
                    location += "/" + l[2]
                if location == "/":
                    location += l[2]
                dirall[location] = 1
    
    if l[0] != "$":
        if location not in dirsiz:
            dirsiz[location] = 0
            dircont[location] = []
        if l[0] == "dir":
            dircont[location] += [location + "/" + l[1]]
        if l[0] != "dir":
            dirsiz[location] += int(l[0])

# sort subsiz
for cool in dirall:
    for a in dirall:
        #todl = []
        for b in dircont:
            if dircont[b] == []:
                # good to calc
                dirtru[b] = dirsiz[b]
                for c in dircont:
                    if not str(dircont[c]).isdigit():
                        t = 0
                        for d in dircont[c]:
                            t += 1
                        if t != 0:
                            for d in tools.rng(t):
                                if dircont[c][d] == b:
                                    dircont[c][d] = dirtru[b]

                dircont[b] = dirtru[b]
            if not str(dircont[b]).isdigit():
                ld = map(lambda x: str(x).isdigit(), dircont[b])
                if all(ld):
                    dirtru[b] = dirsiz[b] + sum(dircont[b])
                    for c in dircont:
                        if not str(dircont[c]).isdigit():
                            t = 0
                            for d in dircont[c]:
                                t += 1
                            if t != 0:
                                for d in tools.rng(t):
                                    if dircont[c][d] == b:
                                        dircont[c][d] = dirtru[b]
                    dircont[b] = dirtru[b]

# count
total = 0
for v in dirtru:
    if dirtru[v] <= 100000:
        total += dirtru[v]

print(total)
targ = 30000000 - (70000000 - dirtru[""])
cur = 70000000
for x in dirtru:
    if dirtru[x] > targ:
        if dirtru[x] < cur:
            cur = dirtru[x]
print(cur)