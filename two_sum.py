# Two Sum
# Given a list of numbers and a target, return the indices of the two numbers that add up to the target.
#
# Time:  O(n)
# Space: O(n)

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Example
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
