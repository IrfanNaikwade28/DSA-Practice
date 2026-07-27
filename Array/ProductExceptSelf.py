nums = [1, 2, 3, 4]
answer = [1] * len(nums)
prefix = [1] * len(nums)
suffix = [1] * len(nums)

# BruteForce Solution
# def ProductExceptSelf(nums):
#     for i in range(len(nums)):
#         prod = 1
#         for j in range(len(nums)):
#             if i != j:
#                 prod *= nums[j]
#         answer.append(prod)


def ProductExceptSelf(nums):
    prod = 1
    for i in range(len(nums)):
        if i > 0:
            prefix[i] = prod * nums[i - 1]
            prod = prefix[i]
        else:
            prefix[i] = 1

    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        if i < len(nums) - 1:
            suffix[i] = prod * nums[i + 1]
            prod = suffix[i]
        else:
            suffix[i] = 1

    for i in range(len(nums)):
        answer[i] = prefix[i] * suffix[i]


ProductExceptSelf(nums)
print(answer)
