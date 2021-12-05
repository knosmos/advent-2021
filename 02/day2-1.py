with open("day2.txt","r") as fin:
    commands = list(map(lambda i:i.split(), fin.read().split("\n")))
x = 0
y = 0
for c in commands:
    a = int(c[1])
    if c[0] == "forward": x += a
    if c[0] == "down": y += a
    if c[0] == "up": y -= a
print(x*y)