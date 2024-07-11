def is_narcissistic(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == number

def find_narcissistic_numbers(range_start, range_end):
    narcissistic_numbers = []
    for number in range(range_start, range_end + 1):
        if is_narcissistic(number):
            narcissistic_numbers.append(number)
    return narcissistic_numbers

range_start = 1
range_end = 10000
narcissistic_numbers = find_narcissistic_numbers(range_start, range_end)
print("Narcissistic numbers between {} and {} are: {}".format(range_start, range_end, narcissistic_numbers))
