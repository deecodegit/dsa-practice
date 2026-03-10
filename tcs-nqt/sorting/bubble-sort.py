def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble_sort([23, 45, 11, 3, 35]))
print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))