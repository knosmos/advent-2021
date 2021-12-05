with open("day3.txt","r") as fin:
    nums = fin.read().split("\n")
k = len(nums[0])
common = [0]*k
for num in nums:
    for i in range(k):
        if num[i] == "1": common[i] += 1
        else: common[i] -= 1
gamma = ""
for c in common:
    if c > 0: gamma += "1"
    else: gamma += "0"
gamma = int(gamma, 2)
epsilon = gamma ^ int("1"*k, 2)
print(gamma*epsilon)