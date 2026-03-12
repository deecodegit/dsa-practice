def octal_to_decimal(octal):
    decimal = 0

    for digit in octal:
        decimal = decimal * 8 + int(digit)
    
    return decimal

print(octal_to_decimal("345"))
print(octal_to_decimal("15"))
print(octal_to_decimal("264"))