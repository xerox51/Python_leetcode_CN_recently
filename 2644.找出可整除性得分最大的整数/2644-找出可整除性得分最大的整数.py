class Solution(object):
    def maxDivScore(self, nums, divisors):
        dct = defaultdict(list)
        for d in divisors:
            dct[len([1 for n in nums if n % d == 0])].append(d)
        return min(dct[max(dct)])        