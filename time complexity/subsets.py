def subsets(nums):
    power_set = []

    def backtrack(start, path):
        power_set.append(path[:]) 

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop() 

    backtrack(0, [])
    return power_set

print(subsets([1, 2, 3])) 
print(subsets([0]))
print(subsets([]))