def threeSumClosest(nums, target):
    nums.sort()
    closestSum = float('inf')

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return currentSum

    return closestSum


nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)  # Output: 2
