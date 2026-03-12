##m1:
def number_to_words(num):

    digit_words = {
        '0': "Zero",
        '1': "One",
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine"
    }

    num_str = str(num)

    result = []

    for digit in num_str:
        result.append(digit_words[digit])

    return " ".join(result)


print(number_to_words(507))

##m2:
def number_to_words_m2(num):

    digit_words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

    digits = []

    while num > 0:
        digit = num % 10
        digits.append(digit_words[digit])
        num = num // 10

    digits.reverse()

    return " ".join(digits)


print(number_to_words_m2(507))