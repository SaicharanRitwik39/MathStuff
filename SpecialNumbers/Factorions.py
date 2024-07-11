import math
def is_factorion(n):
    return n == sum(math.factorial(int(digit)) for digit in str(n))
def find_factorions(limit):
    factorions = []
    for i in range(1, limit):
        if is_factorion(i):
            factorions.append(i)
    return factorions
limit = 50000  
factorions = find_factorions(limit)
print(factorions)
