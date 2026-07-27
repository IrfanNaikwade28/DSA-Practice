nums = [1,2,3]
pos = 0

for i in range(0, len(nums)):
    if nums[i] != 0:
        nums[pos] = nums[i]
        pos += 1

for i in range(pos, len(nums)):
    nums[i] = 0

print(nums)