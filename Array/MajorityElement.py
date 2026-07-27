nums = [2,2,1,1,1,2,2]
minMaj = len(nums)//2

maxCnt = {}
majValue = 0
majKey = 0

for i in nums:
    if i in maxCnt:
        maxCnt[i] += 1
    else:
        maxCnt[i] = 1

for key, val in maxCnt.items():
    if val > majValue:
        majValue = val
        majKey = key


if majValue > minMaj:
    print(majKey)



#Learned about Dict