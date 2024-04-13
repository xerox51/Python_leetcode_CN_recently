from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        l = SortedList()
        for i in range(k):
            l.add(nums[i])
        
        ans = [min(0, l[x - 1])]
        for i in range(k, len(nums)):
            l.remove(nums[i - k])
            l.add(nums[i])
            ans.append(min(0, l[x - 1]))
        return ans