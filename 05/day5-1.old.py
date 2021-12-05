from shapely.geometry import LineString

with open("day5.txt","r") as fin:
    pairs = list(map(lambda i:list(map(lambda j:list(map(int,j.split(","))),i.split(" -> "))), fin.read().split("\n")))
npairs = []
for i in pairs:
    if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
        npairs.append(i)
pairs = npairs
intersects = set()
for i in range(len(pairs)):
    for j in range(i):
        # Very hacky but it should work
        line1 = LineString([pairs[i][0], pairs[i][1]])
        line2 = LineString([pairs[j][0], pairs[j][1]])
        intersect = line1.intersection(line2)
        if intersect:
            try:
                intersects.add((int(intersect.x), int(intersect.y)))
            except AttributeError:
                a, b = intersect.coords
                if a[0] == b[0]:
                    for y in range(int(a[1]), int(b[1]+1)):
                        intersects.add((int(a[0]),int(y)))
                else:
                    for x in range(int(a[0]), int(b[0]+1)):
                        intersects.add((int(x),int(a[1])))
                    #for k in range(int(a[0]),int(b[0]+1)):
                    #    y = ((a[1]-b[1])/(a[0]-b[0]))*(k-a[0]) + a[1]
                    #    if y == int(y):
                    #        intersects.add((int(k),int(y)))
print(intersects)
print(len(intersects))