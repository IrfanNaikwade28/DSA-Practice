nums = [1, 2]


# def FindPeakElem(nums):
#     peakElem = 0
#     i = 0
#     n = len(nums) - 1
#     while i <= n:
#         if n == 0:
#             return peakElem
#         elif i == 0:
#             if nums[i] > nums[i + 1]:
#                 peakElem = i
#         elif i == n:
#             if nums[i] > nums[i - 1]:
#                 peakElem = i
#         elif nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
#             peakElem = i
#         i += 1
#     return peakElem


def FindPeakElem(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if mid == len(nums) - 1:
            return mid
        elif mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            left = mid + 1
        elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return 0


print(FindPeakElem(nums))

# logn with mini conditions
# def findPeakElement(self, nums):
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             mid = (left + right) // 2

#             if nums[mid] < nums[mid + 1]:
#                 left = mid + 1
#             else:
#                 right = mid

#         return left
