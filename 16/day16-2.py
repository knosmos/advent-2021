data = open("day16.txt","r").read()
packet = ""
mapping = {
    "0":"0000",
    "1":"0001",
    "2":"0010",
    "3":"0011",
    "4":"0100",
    "5":"0101",
    "6":"0110",
    "7":"0111",
    "8":"1000",
    "9":"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111"
}
for i in data:
    packet += mapping[i]

def parse():
    global packet

    v = int(packet[:3],2)
    packet = packet[3:]
    t = int(packet[:3],2)
    packet = packet[3:]
 
    #print("version",v,"type",t,"packet",packet)
    if t == 4:
        num = ""
        while True:
            p = packet[:5]
            packet = packet[5:]
            num += p[1:]
            if p[0] == "0": break
        return int(num,2)
    i = packet[0]
    packet = packet[1:]
    subpackets = []
    if i == "0":
        l = int(packet[:15],2)
        packet = packet[15:]
        while l:
            b = len(packet)
            r = parse()
            l -= b - len(packet)
            subpackets.append(r)
    else:
        l = int(packet[:11],2)
        packet = packet[11:]
        for j in range(l):
            b = packet
            r = parse()
            subpackets.append(r)
    if t == 0:
        return sum(subpackets)
    elif t == 1:
        prod = 1
        for i in subpackets: prod *= i
        return prod
    elif t == 2:
        return min(subpackets)
    elif t == 3:
        return max(subpackets)
    elif t == 5:
        return int(subpackets[0] > subpackets[1])
    elif t == 6:
        return int(subpackets[0] < subpackets[1])
    elif t == 7:
        return int(subpackets[0] == subpackets[1])
 
print(parse())