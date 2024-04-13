class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        nn = len(nums)
        
        idxs = [i for i in range(nn)]
        
        tmp = ['' for _ in range(nn)]
        
        res = []
        for k, rLen in queries:
            for i, num in enumerate(nums):
                x = num[-rLen : ]
                tmp[i] = x
            idxs.sort(key = lambda i: (tmp[i], i) )
            res.append(idxs[k - 1])
        return res