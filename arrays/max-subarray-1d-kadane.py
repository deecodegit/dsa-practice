##m1
def max_subarray(nums):
    current_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([1]))
print(max_subarray([5,4,-1,7,8]))

##m2
def max_subarray_optimised(nums):
    current_sum = 0
    max_sum = float('-inf')

    for i in nums:
        current_sum += i
            
        if current_sum > max_sum:
            max_sum = current_sum
            
        if current_sum < 0:
            current_sum = 0

    return max_sum

print(max_subarray_optimised([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray_optimised([1]))
print(max_subarray_optimised([5,4,-1,7,8]))