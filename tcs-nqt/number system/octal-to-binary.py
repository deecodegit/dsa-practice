##m1:
def octal_to_binary(octal):

    mapping = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }
    
    binary = ""

    for digit in octal:
        binary += mapping[digit]

    return binary

print(octal_to_binary("345"))

##m2:
def octal_to_binary_m2(octal):
    decimal = 0

    for digit in octal:
        decimal = decimal * 8 + int(digit)

    binary = ""

    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    
    return binary

print(octal_to_binary_m2("15"))
print(octal_to_binary_m2("264"))  
        
