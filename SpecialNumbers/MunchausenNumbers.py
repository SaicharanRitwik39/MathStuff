#https://pastebin.pl/view/34ea69c2
def is_munchausen_number(num):
    num_str = str(num)
    total = 0
    for digit in num_str:
        total += int(digit) ** int(digit)
    return total == num

def generate_munchausen_numbers(limit):
    munchausen_numbers = []
    for num in range(1, limit + 1):
        if is_munchausen_number(num):
            munchausen_numbers.append(num)
    return munchausen_numbers

limit = 10000
munchausen_numbers = generate_munchausen_numbers(limit)
print(f"Munchausen numbers up to {limit}:")
print(munchausen_numbers)
