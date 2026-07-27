nums =  [2, 4, 8, 9]
k = 3
def placeTheCows(nums, k):
    nums.sort()
    n = len(nums)
    low = 1
    high = nums[n-1] - nums[0]
    ans = 1
    while low<=high:
        mid = (low+high)//2

        if canWePlace(nums, k, mid):
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans

def canWePlace(nums, k, distance):
    cowCount = 1
    lastPlaced = nums[0]

    for i in range(1, len(nums)):
        if nums[i] - lastPlaced >= distance:
            cowCount += 1
            lastPlaced = nums[i]
    if cowCount >= k:
        return True
    else:
        return False

print(placeTheCows(nums,k))
