##m1:
def quick_sort_m1(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[-1]
    left = []
    right = []

    for i in range(len(nums)-1):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])

    return quick_sort_m1(left) + [pivot] + quick_sort_m1(right)

print(quick_sort_m1([5,2,3,1]))
print(quick_sort_m1([5,1,1,2,0,0])) 
print(quick_sort_m1([3,2,1,5,4]))

##m2:
def quick_sort_m2(nums, left, right):
    if left < right:
        p = partition(nums, left, right)

        quick_sort_m2(nums, left, p-1)
        quick_sort_m2(nums, p+1, right)

    return nums


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


arr = [5,2,3,1]
print(quick_sort_m2(arr, 0, len(arr)-1))