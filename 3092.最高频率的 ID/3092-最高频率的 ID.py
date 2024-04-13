from sortedcontainers import SortedList
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        cnt = Counter()
        s1 = SortedList()
        ans = []
        for x,f in zip(nums,freq):
            s1.discard(cnt[x])
            cnt[x] += f
            s1.add(cnt[x])
            ans.append(s1[-1])
        return ans