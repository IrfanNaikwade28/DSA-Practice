nums = [-1, 0, 3, 5, 9, 12]
target = 0


def searchTarget(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            right = mid - 1

        if target > nums[mid]:
            left = mid + 1

    return -1


print(searchTarget(nums, target))
