def sortArray(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    l = nums[:mid]
    r = nums[mid:]  

    sortArray(l)
    sortArray(r)    

    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            nums[k] = l[i]
            i += 1
        else:
            nums[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        nums[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        nums[k] = r[j]
        j += 1
        k += 1 

    return nums

print(sortArray([5,2,3,1]))
print(sortArray([5,1,1,2,0,0]))
print(sortArray([3,2,1,5,4]))


