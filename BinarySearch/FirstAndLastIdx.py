nums = [8]
target = 8


def findFirstIdx(nums, target):
    left = 0
    right = len(nums) - 1
    start = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            start = mid
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return start


def findLastIdx(nums, target):
    left = 0
    right = len(nums) - 1
    end = len(nums)

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
            end = mid
        else:
            left = mid + 1
    return end


def FirstAndLastIdx(nums, target):
    start = findFirstIdx(nums, target)
    if start == -1:
        return [-1, -1]

    end = findLastIdx(nums, target) - 1
    return [start, end]


print(FirstAndLastIdx(nums, target))
