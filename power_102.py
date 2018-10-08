def power(m, n):
    if n == 0:
        return 1

    power_n_minus_1 = power(m, n - 1)
    return m * power_n_minus_1