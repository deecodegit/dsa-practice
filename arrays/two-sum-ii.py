def two_sum_ii(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:
        sum = nums[i] + nums[j]

        if sum == target:
            return [i+1, j+1]
        elif sum < target:
            i += 1
        else:
            j -= 1
    return None

print(two_sum_ii([2, 7, 11, 15], target=9))
print(two_sum_ii([2, 3, 4], target=6))
print(two_sum_ii([-1, 0], target=-1))