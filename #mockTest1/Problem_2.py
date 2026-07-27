nums = [100, 4, 200, 1, 3, 2]


# O(nlogn) Solution
def LongestConsecutiveSequence(nums):
    if len(nums) == 0:
        return 0
    nums = set(nums)
    nums = list(nums)
    nums.sort()

    cntLen = 1
    prev = 1
    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            cntLen += 1
        else:
            if cntLen > prev:
                prev = cntLen
            cntLen = 1

    return max(prev, cntLen)


print(LongestConsecutiveSequence(nums))


# O(n) solution:
# def longestConsecutive(nums):
# if not nums:
#     return 0

# numSet = set(nums)
# longest = 0

# for num in numSet:

#     # Start only from the beginning of a sequence
#     if num - 1 not in numSet:

#         current = num
#         length = 1

#         while current + 1 in numSet:
#             current += 1
#             length += 1

#         longest = max(longest, length)

# return longest
