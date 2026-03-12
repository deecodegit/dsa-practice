##m1:
def decimal_to_bianry_m1(n):
    if n == 0 or n == 1:
        return str(n)
    
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    
    return binary

print(decimal_to_bianry_m1(10))
print(decimal_to_bianry_m1(15))

##m2:
def decimal_to_binary_m2(n):
    if n == 0 or n == 1:
        return str(n)
    
    remainder = []
    while n > 0:
        remainder.append(str(n % 2))
        n = n // 2
    
    return "".join(reversed(remainder))

print(decimal_to_binary_m2(10))
print(decimal_to_binary_m2(15))