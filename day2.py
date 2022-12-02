import sys

inp = []
for l in sys.stdin:
    inp += [l[:-1].split(" ")]

print(inp)

matchup = {
    "A": {
        "X":4,
        "Y":8,
        "Z":3
    },
    "B": {
        "X":1,
        "Y":5,
        "Z":9
    },
    "C": {
        "X":7,
        "Y":2,
        "Z":6
    }
}

matchup_pt2 = {
    "A": {
        "X":3,
        "Y":4,
        "Z":8
    },
    "B": {
        "X":1,
        "Y":5,
        "Z":9
    },
    "C": {
        "X":2,
        "Y":6,
        "Z":7
    }
}

total = 0
total_2 = 0

for round in inp:
    total += matchup[round[0]][round[1]]
    total_2 += matchup_pt2[round[0]][round[1]]

print(f"Part 1: {total}")
print(f"Part 2: {total_2}")