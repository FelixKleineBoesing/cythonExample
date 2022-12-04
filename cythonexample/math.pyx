cimport cython

def fibonacci(int n):
    # calculates nth number of fibonacci sequence
    cdef int fibo_num = 0
    cdef int last_num = 1
    cdef int i
    for i in range(n):

