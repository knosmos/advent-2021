fin = open("day8.txt","r").read().split("\n")
data = []
for i in range(len(fin)):
    display = list(map(lambda j:j.split(), fin[i].split(" | ")))
    for j in range(10):
        display[0][j] = "".join(sorted(list(display[0][j])))
    for j in range(4):
        display[1][j] = "".join(sorted(list(display[1][j])))
    data.append(display)
res = 0
for display in data:
    digits = display[0]
    for i in digits:
        # ONE = len 2
        if len(i) == 2: ONE = i
        # FOUR = len 4
        if len(i) == 4: FOUR = i
        # SEVEN = len 3
        if len(i) == 3: SEVEN = i
        # EIGHT = len 7
        if len(i) == 7: EIGHT = i

    # SIX = len 6 that has exactly 1 segment of 1
    for i in digits:
        if len(i) == 6:
            if (ONE[0] in i or ONE[1] in i) and not (ONE[0] in i and ONE[1] in i):
                SIX = i
    # Missing segment of SIX = c
    for seg in EIGHT:
        if not seg in SIX:
            c = seg
            break
    # FIVE = len 5 without c
    for i in digits:
        if len(i) == 5:
            if not c in i:
                FIVE = i
    # Other missing segment of FIVE = e
    for seg in EIGHT:
        if seg != c and not seg in FIVE:
            e = seg
    # NINE = len 6 without e
    for i in digits:
        if len(i) == 6 and not e in i:
            NINE = i
    # TWO = len 5 with e
    for i in digits:
        if len(i) == 5 and e in i:
            TWO = i
    # THREE = len 5 that is not TWO or FIVE
    for i in digits:
        if len(i) == 5 and i != TWO and i != FIVE:
            THREE = i
    # ZERO = len 6 with e
    for i in digits:
        if len(i) == 6 and e in i and i != SIX:
            ZERO = i
    # NINE = len 6 without e
    for i in digits:
        if len(i) == 6 and not (e in i):
            NINE = i
    decoded = {
        ZERO: 0,
        ONE: 1,
        TWO: 2,
        THREE: 3,
        FOUR: 4,
        FIVE: 5,
        SIX: 6,
        SEVEN: 7,
        EIGHT: 8,
        NINE: 9
    }
    r = 0
    for digit in display[1]:
        r *= 10
        r += decoded[digit]
    res += r
print(res)