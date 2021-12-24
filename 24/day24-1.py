data = [i.split() for i in open("day24.txt","r").read().split("\n")]
sections = []
k = []
for line in data:    
    k.append(line)
    print(k)
    if line == ["add","z","y"]:
        sections.append(k)
        k = []
print(sections)

mem = {}

def run(w,z,num):
    vars = {"w":0, "x":0, "y":0, "z":0}
    c = 0
    if len(num) >= 15: return
    data = sections[len(num)-1]
    for line in data:
        if len(line) == 2:
            vars[line[1]] = w
            continue
        try:
            b = int(line[2])
        except:
            b = vars[line[2]]
        a = line[1]
        if line[0] == "add":
            vars[a] += b
        if line[0] == "mul":
            vars[a] *= b
        if line[0] == "div":
            vars[a] //= b
        if line[0] == "mod":
            vars[a] %= b
        if line[0] == "eql":
            vars[a] = int(vars[a]==b)
    if len(num) == 14:
        if num[9:] == "11111" or vars["z"] == 0:
            print(num,vars["z"])
        return num
    for w2 in range(9,0,-1):
        n2 = num
        n2 += str(w2)
        run(w2,vars["z"],n2)

for i in range(9,0,-1):
    run(i,0,str(i))