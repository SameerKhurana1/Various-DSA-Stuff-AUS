# Binary Search
# Search a sorted array by repeatedly halving the search space.
#
# Time:  O(log n)
# Space: O(1)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))   # Output: 3
print(binary_search(arr, 6))   # Output: -1
