##m1:
def max_circular_subarray_sum(arr):
    max_sum = min_sum = arr[0]
    total_sum  = cmin = cmax = 0

    for i in arr:
        cmax = max(i, cmax + i)
        max_sum = max(max_sum, cmax)

        cmin = min(i, cmin + i)
        min_sum = min(min_sum, cmin)

        total_sum += i

    if max_sum < 0:
        return max_sum
        
    return max(max_sum, total_sum - min_sum)

print(max_circular_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
print(max_circular_subarray_sum([1]))
print(max_circular_subarray_sum([5,4,-1,7,8]))

##m2:
def kadane_with_indices(arr, findMax=True):
    n = len(arr)
    
    cbest = arr[0]
    obest = arr[0]
    start = end = s = 0

    for i in range(1, n):
        
        if (arr[i] > cbest + arr[i]) if findMax else (arr[i] < cbest + arr[i]):
            cbest = arr[i]
            s = i
        else:
            cbest += arr[i]

        if (cbest > obest) if findMax else (cbest < obest):
            obest = cbest
            start = s
            end = i

    return obest, start, end  

def max_circular_subarray_sum_indices(arr):
    total_sum = sum(arr)

    max_sum, max_l, max_r = kadane_with_indices(arr, True)
    min_sum, min_l, min_r = kadane_with_indices(arr, False)

    if max_sum < 0:
        return max_sum, max_l, max_r

    wrap_sum = total_sum - min_sum

    if wrap_sum > max_sum:
        n = len(arr)
        start = (min_r + 1) % n
        end = (min_l - 1 + n) % n
        return wrap_sum, start, end
    else:
        return max_sum, max_l, max_r
    
print(max_circular_subarray_sum_indices([-2,1,-3,4,-1,2,1,-5,4]))
print(max_circular_subarray_sum_indices([1]))
print(max_circular_subarray_sum_indices([5,4,-1,7,8]))