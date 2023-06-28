def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num >= start:
            if num == start:
                start += 1
            else:
                result.append([start, num - 1])
                start = num + 1

    if start <= upper:
        result.append([start, upper])

    return result


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)  # Output: [[2, 2], [4, 49], [51, 74], [76, 99]]
