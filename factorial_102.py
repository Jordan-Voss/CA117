def factorial(n):
    if n == 0:
        return 1

    facotrial_n_minus_1 = factorial(n - 1)
    return n * facotrial_n_minus_1