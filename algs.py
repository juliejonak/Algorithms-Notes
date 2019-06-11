# assume positive integers as n
# 0! = 1
# Return a numerical value

def iter_factorial(n):
    result = 1
    # loop until 1
    while n > 1:
        # multiply
        result *= n
        n -= 1
    
    return result

n = 4
print('Result when n is', n, 'is: ', iter_factorial(n))


# def rec_factorial(n):

# def iter_fib(n):

# def rec_fib(n):