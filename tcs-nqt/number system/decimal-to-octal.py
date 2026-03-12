##m1:
def decimal_to_octal_m1(n):
    if n == 0 or n == 1:
        return str(n)
    
    octal = ""

    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n = n // 8
    
    return octal

print(decimal_to_octal_m1(10))
print(decimal_to_octal_m1(15))
print(decimal_to_octal_m1(264))

##m2:
def decimal_to_octal_m2(n):
    if n == 0 or n == 1:
        return str(n)
    
    remainder = []
    while n > 0:
        remainder.append(str(n % 8))
        n = n // 8
    
    return "".join(reversed(remainder))

print(decimal_to_octal_m2(10))
print(decimal_to_octal_m2(15))
print(decimal_to_octal_m2(264))