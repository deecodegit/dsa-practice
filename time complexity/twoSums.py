##m1:
def twoSumM1(nums, target):
    seen = {}

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
            
print(twoSumM1([2, 7, 11, 15], 9)) 

##m2:
def twoSumM2(nums, target):
    seen = {}

    for i, nums in enumerate(nums):
        complement = target - nums

        if complement in seen:
            return (seen[complement], i)
        seen[nums] = i

print(twoSumM2([2, 7, 11, 15], 9)) 

##m3:
def twoSumM3(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return (seen[complement], i)
        seen[nums[i]] = i

print(twoSumM3([2, 7, 11, 15], 9)) 