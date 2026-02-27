def searchNSA(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        
        if mid - 1 >= low and nums[mid - 1] == target:
            return mid - 1
        
        if mid + 1 < len(nums) and nums[mid + 1] == target:
            return mid + 1
        
        if nums[mid] > target:
            high = mid - 2
        else:
            low = mid + 2
        
    return -1

print(searchNSA([1, 2, 3, 4, 5], 3))
print(searchNSA([1, 3, 2, 4, 5], 3))
print(searchNSA([1, 2, 4, 3, 5], 3))
print(searchNSA([1, 2, 3, 5, 4], 3))