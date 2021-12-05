with open("day3.txt","r") as fin:
    nums = fin.read().split("\n")
    nums2 = nums.copy()
k = len(nums[0])
oxy = ""
co2 = ""
for i in range(k):
    common = 0
    for num in nums:
        if num[i] == "1": common += 1
        else: common -= 1
    if common >= 0: oxy += "1"
    if common < 0: oxy += "0"
    filtered = []
    for num in nums:
        if num[i] == oxy[i]:
            filtered.append(num)
    nums = filtered
    if len(nums) == 1:
        oxy = nums[0]
        break
nums = nums2
for i in range(k):
    common = 0
    for num in nums:
        if num[i] == "1": common += 1
        else: common -= 1
    if common < 0: co2 += "1"
    if common >= 0: co2 += "0"
    filtered = []
    for num in nums:
        if num[i] == co2[i]:
            filtered.append(num)
    nums = filtered
    if len(nums) == 1:
        co2 = nums[0]
        break
#print(oxy,co2)
oxy = int(oxy, 2)
co2 = int(co2, 2)
#print(oxy,co2)
print(oxy*co2)