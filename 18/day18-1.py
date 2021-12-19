import json
import math
from rich import print
nums = []
for i in open("day18.txt","r").readlines():
    nums.append(json.loads(i))

def insert_l(num, i, l):
    j = i-1
    if j < 0:
        return num, False
    if type(num[j]) == int:
        num[j] += l
        return num, True
    else:
        k = insert_l(num[j], len(num[j]), l)
        if k[1]:
            return num[:j] + [k[0]] + num[j+1:], True
    return num, False

def insert_r(num, i, r):
    j = i+1
    if j > len(num)-1:
        return num, False
    if type(num[j]) == int:
        num[j] += r
        return num, True
    else:
        k = insert_r(num[j], -1, r)
        if k[1]:
            return num[:j] + [k[0]] + num[j+1:], True
    return num, False

def explode(num, depth):
    changed = False
    lsum = 0
    rsum = 0
    if depth == 4:
        for i in range(len(num)):
            if type(num[i]) == list:
                left = num[i][0]
                right = num[i][1]

                k = insert_l(num, i, left)
                if k[1]:
                    num = k[0]
                else:
                    lsum += left

                k = insert_r(num, i, right)
                if k[1]:
                    num = k[0]
                else:
                    rsum += right

                num = num[:i] + [0] + num[i+1:]
                return num, True, lsum, rsum
    for i in range(len(num)):
        if type(num[i]) == list:
            n, c, l, r = explode(num[i], depth+1)
            k = insert_l(num, i, l)
            if k[1]:
                num = k[0]
            else:
                lsum += l
            k = insert_r(num, i, r)
            if k[1]:
                num = k[0]
            else:
                rsum += r
            num = num[:i] + [n] + num[i+1:]
            if c:
                changed = True
                break
    return num, changed, lsum, rsum

def split(num):
    changed = False
    for i in range(len(num)):
        if type(num[i]) == int:
            if num[i] > 9:
                num[i] = [math.floor(num[i]/2), math.ceil(num[i]/2)]
                changed = True
                break
        else:
            num[i], c = split(num[i])
            if c:
                changed = True
                break
    return num, changed

def magnitude(num):
    if type(num) == int:
        return num
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])

num = nums[0]
for i in nums[1:]:
    num = [num, i]
    #print("addition:",num)
    c1 = True
    c2 = True
    while c1 or c2:
        num, c1, l, r = explode(num,1)
        #print("explode:",num)
        while c1:
            num, c1, _, _ = explode(num,1)
            #print("explode:",num)
        num, c2 = split(num)
        if c2:
            pass
            #print("split:",num)
    #print(num)
print(magnitude(num))