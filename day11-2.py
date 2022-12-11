import sys, tools

inp = [[]]
for l in sys.stdin:
    if l == "\n":
        inp += [[]]
    if l != "\n":
        inp[-1] += l[:-1].strip().split(":")

monk = []
bignum = 1
for l in inp:
    m = {}
    m["num"] = int(l[0].split(" ")[1])
    m["holding"] = list(map(int, l[3].split(",")))
    m["op"] = l[5].split("=")[1].strip()
    m["tst"] = int(l[7].split("by")[1])
    m["tru"] = int(l[9].split("y ")[1])
    m["fal"] = int(l[11].split("y ")[1])
    m["count"] = 0
    bignum *= m["tst"]
    monk += [m]

for r in tools.norng(10000):
    for m in monk:
        for hold in m["holding"]:
            m["count"] += 1
            if m["op"] == "old * old":
                hold = hold * hold
            if m["op"] != "old * old":
                op = m["op"].split(" ")
                if op[1] == "+":
                    hold = hold + int(op[2])
                if op[1] == "*":
                    hold = hold * int(op[2])
            hold = hold % bignum
            if hold % m["tst"] == 0:
                monk[m["tru"]]["holding"] += [hold]
            if hold % m["tst"] != 0:
                monk[m["fal"]]["holding"] += [hold]
        
        m["holding"] = []

mcounts = [x["count"] for x in monk]
mcounts.sort()
print(mcounts[-1]*mcounts[-2])