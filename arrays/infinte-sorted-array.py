def ISA(nums, target):
    low = 0
    high = 1

    while target > nums[high]:
        low = high
        high *= 2

    return binarySearchM1(nums, target, low, high)

def binarySearchM1(nums, target, low, high): 
    while low <= high:
        mid = (low + high) // 2

        if mid >= len(nums):
            high = mid - 1
            continue

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
   
    return -1

print(ISA([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(ISA([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
print(ISA([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
