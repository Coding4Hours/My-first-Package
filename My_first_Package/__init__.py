from math import factorial as fact

def permutations(n: int, k: int) -> int:
    return fact(n) // fact(n - k)

def combinations(n: int, k: int) -> int:
    return fact(n) // (fact(k) * fact(n - k))

def calculate_regions(lines: int) -> int:
    return (lines * (lines + 1)) // 2 + 1

def fibonacci(num: int) -> int:
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def prime_factors(num: int) -> int:
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors


def gcd(num1: int, num2: int) -> int:
    while num2:
        num1, num2 = num2, num1 % num2
    return a


def lcm(num1: int, num2: int) -> int:
    return abs(num1 * num2) // gcd(num1, num2)
