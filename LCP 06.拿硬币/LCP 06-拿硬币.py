class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        ans = 0
        for item in coins:
          if item%2 == 0:
            ans += item//2
          else:
            ans += item//2 + 1
        return ans