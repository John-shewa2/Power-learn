# Large power
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False


print(large_power(500, 2))


# Divisible by ten
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


print(divisible_by_ten(30))
