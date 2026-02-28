def kadane_indices(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    return max_sum, start, end

print(kadane_indices([-2,1,-3,4,-1,2,1,-5,4]))
print(kadane_indices([1]))
print(kadane_indices([5,4,-1,7,8]))
