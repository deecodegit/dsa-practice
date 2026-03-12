def binary_to_octal(binary):
    result = ""
    i = len(binary)

    while i > 0:
        group = binary[max(0, i-3): i]
        decimal = 0

        for digit in group:
            decimal = decimal * 2 + int(digit)

        result = str(decimal) + result
        i -= 3

    return result

print(binary_to_octal("110101101"))
print(binary_to_octal("101010"))