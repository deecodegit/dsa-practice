def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2

    while low <= high:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch([1, 2, 3, 4, 5], 3))