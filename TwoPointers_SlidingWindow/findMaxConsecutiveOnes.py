nums = [1, 1, 0, 1, 1, 1]

# Sliding window approach TC O(n)
def findMaxConsecutiveOnes(nums):
    left = 0
    maxCnt = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            left = right + 1
        else:
            maxCnt = max(maxCnt, right - left + 1)

    return maxCnt


print(findMaxConsecutiveOnes(nums))

# O(n) of two tracking vars.. brutforce method
# def findMaxConsecutiveOnes(nums):
#     prevCnt = 0
#     currCnt = 0

#     for i in range(len(nums)):
#         if nums[i] == 1:
#             currCnt += 1
#         else:
#             currCnt = 0

#         prevCnt = max(prevCnt, currCnt)

#     return prevCnt
