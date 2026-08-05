nums = [-1, 0, 1, 2, -1, -4]

# bruforce with n^3
# def threeSum(nums):
#     n = len(nums)
#     ans = []
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 tripletSum = nums[i] + nums[j] + nums[k]
#                 sumArr = [nums[i], nums[j], nums[k]]
#                 sumArr.sort()
#                 if tripletSum == 0 and sumArr not in ans:
#                     ans.append(sumArr)
#     return ans



# Optimized Soln of O(n^2)
def threeSum(nums):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n-2):
        left = i + 1
        right = n - 1
        target = -nums[i]
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while left < right:
            if nums[left] + nums[right] == target:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
               left+=1
            else:
               right-=1

    return ans


print(threeSum(nums))
