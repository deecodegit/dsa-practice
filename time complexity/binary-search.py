##m1:
def binarySearchM1(nums, target):
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

print(binarySearchM1([1, 2, 3, 4, 5], 3))

##m2
def binarySearchM2(nums, target):
    low = 0
    high = len(nums) - 1
        
    while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
            
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
print(binarySearchM2([1, 2, 3, 4, 5], 3))