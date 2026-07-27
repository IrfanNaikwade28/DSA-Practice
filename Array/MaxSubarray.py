# nums = [-2,1,-3,4,-1,2,1,-5,4]


# def maxSubArray(nums):
#     maxSum = float('-inf')
#     n = len(nums)
#     subArrmaxSum = 0

#     if n == 1:
#         return nums[0] 

#     for i in range(0, n):          
#         if subArrmaxSum < 0:
#             continue
#         for j in range(i, n):
#             subArrmaxSum = subArrmaxSum + nums[j]
#             maxSum = max(maxSum, subArrmaxSum)
#     return maxSum

# print(maxSubArray(nums))


nums = [-2,1,-3,4,-1,2,1,-10,4]

def maxSubArray(nums):
    maxSum = float('-inf')
    n = len(nums)
    subArrmaxSum = 0
    start = 0
    end = -1
    tempStart = 0

    for i in range(0, n):
        subArrmaxSum += nums[i]

        if subArrmaxSum > maxSum:
            maxSum = subArrmaxSum
            end = i
            start = tempStart

        if subArrmaxSum < 0:
            subArrmaxSum = 0
            tempStart = i + 1

    return maxSum, start, end

print(maxSubArray(nums))