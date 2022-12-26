def fib(n):
    """Returns n-th element of the Fibonacci series"""

    if (n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

