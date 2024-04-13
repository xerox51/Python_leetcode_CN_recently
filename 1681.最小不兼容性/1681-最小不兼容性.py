from typing import *


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf] * (1 << n)
        dp[0] = 0
        group = n // k
        values = {}

        for mask in range(1 << n):
            if mask.bit_count() != group:
                continue
            mn = 20
            mx = 0
            cur = set()
            for i in range(n):
                if mask & (1 << i) > 0:
                    if nums[i] in cur:
                        break
                    cur.add(nums[i])
                    mn = min(mn, nums[i])
                    mx = max(mx, nums[i])
            if len(cur) == group:
                values[mask] = mx - mn

        for mask in range(1 << n):
            if dp[mask] == inf:
                continue
            seen = {}
            for i in range(n):
                if mask & (1 << i) == 0:
                    seen[nums[i]] = i
            if len(seen) < group:
                continue
            sub = 0
            for v in seen:
                sub |= 1 << seen[v]
            nxt = sub
            while nxt > 0:
                if nxt in values:
                    dp[mask | nxt] = min(dp[mask | nxt], dp[mask] + values[nxt])
                nxt = (nxt - 1) & sub

        return dp[-1] if dp[-1] < inf else -1