def max_submatrix(matrix):
    max_sum = float('-inf')
    rows = len(matrix)
    cols = len(matrix[0])

    for left in range(cols):
        temp = [0] * rows

        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            current_sum = temp[0]
            best = temp[0]

            for i in range(1, rows):
                current_sum = max(temp[i], current_sum + temp[i])
                best = max(best, current_sum)
            max_sum = max(max_sum, best)   
    
    return max_sum

print(max_submatrix([[1, -2, -1, 4], [-8, 3, 4, 2], [3, 8, 10, -8], [-4, -1, 1, 7]]))
print(max_submatrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
print(max_submatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
