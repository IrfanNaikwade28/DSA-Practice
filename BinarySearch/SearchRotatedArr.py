nums = [5, 6, 1, 2, 3, 4]
target = 6


# My brutforce but O(logn) solution
def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left


def searchTarget(start, end, nums, target):
    left = start
    right = end

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            right = mid - 1

        if target > nums[mid]:
            left = mid + 1

    return -1


def SearchRotatedArr(nums, target):
    start = findMin(nums)
    right = searchTarget(start, len(nums) - 1, nums, target)
    left = searchTarget(0, start - 1, nums, target)

    if right != -1:
        return right
    else:
        return left


print(findMin(nums))


# Optimized in Single Binary Search
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
