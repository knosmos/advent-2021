lines = open("day20.txt","r").read().split("\n")
alg = lines[0]
data = lines[2:]

def enhance(data):
    n = len(data)
    l = len(data[0])
    # Pad outer ring of data with .s
    data = ["."*(n+20) for _ in range(10)] + ["."*10+i+"."*10 for i in data] + ["."*(n+20) for _ in range(10)]
    # ENHANCE
    output = []
    for i in range(1,len(data)-1):
        line = []
        for j in range(1,len(data)-1):
            square = [
                data[i-1][j-1],
                data[i-1][j],
                data[i-1][j+1],

                data[i][j-1],
                data[i][j],
                data[i][j+1],

                data[i+1][j-1],
                data[i+1][j],
                data[i+1][j+1]
            ]
            num = "".join(["0" if k == "." else "1" for k in square])
            #print(num)
            num = int(num,2)
            #print(num)
            out = alg[num]
            line.append(out)
        output.append("".join(line))
    return output

for i in range(25):
    for _ in range(2):
        data = enhance(data)
    data = data[10:-10]
    data = [i[10:-10] for i in data]
print(sum([i.count("#") for i in data]))