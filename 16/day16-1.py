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
    if len(packet) == 0:
        return 0
 
    v = int(packet[:3],2)
    packet = packet[3:]
    t = int(packet[:3],2)
    packet = packet[3:]
 
    # print("version",v,"type",t,"packet",packet)
    if t == 4:
        num = ""
        while True:
            p = packet[:5]
            packet = packet[5:]
            num += p[1:]
            if p[0] == "0": break
        # print(num)
        return v,int(num,2)
    else:
        i = packet[0]
        packet = packet[1:]
        if i == "0":
            l = int(packet[:15],2)
            packet = packet[15:]
            num = 0
            while l:
                b = len(packet)
                r = parse()
                l -= b - len(packet)
                num += r[1]
                v += r[0]
            return v, num
        else:
            l = int(packet[:11],2)
            packet = packet[11:]
            # print(packet)
            # print("num packets: ",l)
            num = 0
            for j in range(l):
                r = parse()
                num += r[1]
                v += r[0]
            return v, num
 
print(parse()[0])