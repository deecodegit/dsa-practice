def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([23, 45, 11, 3, 35]))
print(selection_sort([5, 1, 4, 2, 8]))  
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))