class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans, st = 0, []
        for num in nums:
            max_t = 0
            while st and st[-1][0] <= num:
                max_t = max(max_t, st.pop()[1])
            max_t = max_t + 1 if st else 0
            ans = max(ans, max_t)
            st.append((num, max_t))
        return ans