def same_2_pointer(nums, target):
    left = 0
    for right in range(len(nums)):
        if nums[right] < target:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

print(same_2_pointer([1, 2, 3, 4, 5], target=3))
print(same_2_pointer([5, 4, 3, 2, 1], target=3))
print(same_2_pointer([1, 3, 2, 5, 4], target=3))