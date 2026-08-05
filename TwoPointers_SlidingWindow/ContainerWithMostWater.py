height = [1,8,6,2,5,4,8,3,7]

def ContainerWithMostWater(height):
    left = 0
    right = len(height) - 1
    maxWater = 0
    while left < right:
        width = right - left
        water_amount = width * min(height[left], height[right])
        maxWater = max(maxWater, water_amount)

        if height[left] > height[right]:
            right-=1
        else:
            left+=1

    return maxWater

print(ContainerWithMostWater(height))
