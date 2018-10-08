def fibonacci(N):
    if N == 0 or N == 1:
        return 1

    return fibonacci(N - 1) + fibonacci(N - 2)