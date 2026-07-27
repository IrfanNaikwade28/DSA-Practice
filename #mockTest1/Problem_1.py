nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


def removeElem(nums, val):
    cnt = 0
    idx = 0
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] != val:
            nums[idx] = nums[i]
            idx += 1
            cnt += 1
        i += 1
    return cnt


print(removeElem(nums, val))
print(nums)
