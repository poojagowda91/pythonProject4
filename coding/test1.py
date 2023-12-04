# input = 123
# output = largest value : 321


def large_num(num):
    number_str = str(num)
    sorted_digits = sorted(number_str, reverse=True)
    largest_number = int(''.join(sorted_digits))
    print("The largest number : ", largest_number)


number = 546
large_num(number)


