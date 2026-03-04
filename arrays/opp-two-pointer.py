def opp_2_pointer(nums, target=0):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return None

print(opp_2_pointer([-4, -3, -2, -1, 0, 1, 2, 5], target=1))
print(opp_2_pointer([-4, -3, -2, -1, 0, 1, 2, 3], target=-5))
print(opp_2_pointer([-4, -3, -2, -1, 0, 1, 2, 4], target=-6))
