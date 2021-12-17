x1 = 257
x2 = 286
y1 = -101
y2 = -57

m = 0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        x = a
        y = b
        pos = [0,0]
        for i in range(1000):
            pos[0] += x
            pos[1] += y
            x = x-1 if x > 0 else x+1 if x < 0 else x
            y -= 1
            if pos[0] >= x1 and pos[0] <= x2 and pos[1] >= y1 and pos[1] <= y2:
                m += 1
                break
            if x > 0 and pos[0] > x2:
                break
            if x < 0 and pos[0] < x1:
                break
            if y < 0 and pos[1] < y1:
                break
print(m)