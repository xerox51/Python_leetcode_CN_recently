class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        f = [0] * n
        f[0] = 1
        cnt_a = 0
        for i, v in enumerate(f):
            if i + delay >= n:
                cnt_a += v
            for j in range(i + delay, min(i + forget, n)):
                f[j] = (f[j] + v) % MOD
        return (cnt_a + f[-1]) % MOD