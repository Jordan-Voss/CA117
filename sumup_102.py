def sumup(n):
    if n == 0:
        return 0
    
    sum_to_n_minus_1 = sumup(n-1)
    return n + sum_to_n_minus_1
