# Sliding Window — Maximum Sum Subarray of size k
# Find the maximum sum of any contiguous subarray of size k.
#
# Time:  O(n)
# Space: O(1)

def max_sum_subarray(nums, k):
    if len(nums) < k:
        return None

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Example
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))  # Output: 9
