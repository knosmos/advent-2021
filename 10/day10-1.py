data=open("day10.txt","r").read().split("\n")
res = 0
for line in data:
    stack = []
    for char in line:
        if char in "{[(<":
            stack.append(char)
        else:
            if {"{":"}","[":"]","(":")","<":">"}[stack[-1]] != char:
                res += {")":3,"]":57,"}":1197,">":25137}[char]         
                break
            else:
                stack.pop()
print(res)