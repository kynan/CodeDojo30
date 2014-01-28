class Fibonacci(object):
    _cache = {0: 1, 1: 2}

    def __init__(self, n):
        self.n = n

    def get(self, n):
        if not n in Fibonacci._cache:
            Fibonacci._cache[n] = self.get(n-1) + self.get(n-2)
        return Fibonacci._cache[n]

    def next(self):
        return Fibonacci(self.n + 1)

    def __iter__(self):
        while True:
            yield self.get(self.n)
            self.n += 1


def fibrepr(n):
    def fib_iter(n, fib, l):
        for i, f in enumerate(fib):
            if f == n:
                yield '1' + i*'0' + l
            elif n > f:
                for match in fib_iter(n - f, fib.next(), '1' + i*'0' + l):
                    yield match
            else:
                break
    return fib_iter(n, Fibonacci(0), '')
