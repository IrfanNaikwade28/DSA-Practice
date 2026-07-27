nums = [5, 7, 7, 8, 8, 8, 10]
target = 8


def findUpperBound(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (right + left) // 2

        if nums[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


print(findUpperBound(nums, target))
