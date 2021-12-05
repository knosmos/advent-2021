with open("day2.txt","r") as fin:
    commands = list(map(lambda i:i.split(), fin.read().split("\n")))
aim = 0
x = 0
y = 0
for c in commands:
    a = int(c[1])
    if c[0] == "forward":
        x += a
        y += aim*a
    if c[0] == "down": aim += a
    if c[0] == "up": aim -= a
print(x*y)