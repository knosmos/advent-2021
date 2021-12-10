data=open("day10.txt","r").read().split("\n")
res = []
for line in data:
    stack = []
    for char in line:
        if char in "{[(<":
            stack.append(char)
        else:
            if {"{":"}","[":"]","(":")","<":">"}[stack[-1]] != char:
                break
            else:
                stack.pop()
    else:
        completion = stack[::-1]
        r = 0
        for i in completion:
            r *= 5
            r += {"(":1,"[":2,"{":3,"<":4}[i]
        res.append(r)
res = sorted(res)[len(res)//2]
print(res)