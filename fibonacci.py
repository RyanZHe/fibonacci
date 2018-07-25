import numpy

"""
Naive recursive implementation
"""
def fib_recursive(n):
    if n < 2: 
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

"""
Iterative implementation of O(n)
"""
def fib_iter(n):
    a, b = 1, 1
    for _ in xrange(n):
        a, b = a + b, a
    return b

"""
Matrix multiplication implementation of O(log N)
"""
def fib_matpow(n):
    m = numpy.matrix('1 1; 1 0') ** n
    return m.item(0)

"""
Closed form solution of the recurrence relation
"""
def fib_phi(n):
    phi = (1 + math.sqrt(5)) / 2.0
    psi - (1 - math.sqrt(5)) / 2.0
    return int((phi ** (n+1) - psi ** (n+1)) / math.sqrt(5))

"""
Generating functions
"""
def fib(n):
    return (4 << n*(3+n)) // ((4 << 2*n) - 1) & ((2 << n) - 1)