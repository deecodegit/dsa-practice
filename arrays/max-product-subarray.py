def max_product_subarray(nums):
    max_prev = min_prev = result = nums[0]

    for i in range(1, len(nums)):
        temp_max = max(nums[i], max_prev * nums[i], min_prev * nums[i])
        temp_min = min(nums[i], max_prev * nums[i], min_prev * nums[i])

        max_prev = temp_max
        min_prev = temp_min

        result = max(result, max_prev)

    return result

print(max_product_subarray([2,3,-2,4]))
print(max_product_subarray([-2,0,-1]))
print(max_product_subarray([-2,3,-4]))
