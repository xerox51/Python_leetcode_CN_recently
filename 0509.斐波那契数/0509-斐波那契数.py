class Solution:
    def fib(self, n: int) -> int:
        @cache
        def fibnacci(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibnacci(n-1) + fibnacci(n-2)
        return fibnacci(n)

