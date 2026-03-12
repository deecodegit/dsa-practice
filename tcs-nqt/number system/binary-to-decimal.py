##m1:
def binary_to_decimal_m1(binary):
    decimal = 0
    power = 0

    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1
    
    return decimal

print(binary_to_decimal_m1("1010")) 
print(binary_to_decimal_m1("1111"))

##m2:
def binary_to_decimal_m2(binary):
    decimal = 0

    for digit in binary:
        decimal = decimal * 2 + int(digit)
    
    return decimal

print(binary_to_decimal_m2("1010"))
print(binary_to_decimal_m2("1111"))