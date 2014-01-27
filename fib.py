def fibrepr(n):
    fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    def fib_iter(n, fibs, l):
        for i, f in enumerate(fibs):
            if f == n:
                yield '1' + i*'0' + l
            elif n > f:
                for fib in fib_iter(n - f, fibs[i+1:], '1' + i*'0' + l):
                    yield fib
            else:
                break
    return fib_iter(n, fibs, '')
