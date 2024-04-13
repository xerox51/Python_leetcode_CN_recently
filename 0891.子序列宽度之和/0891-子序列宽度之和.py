class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        arr = sorted(nums)
        n = len(arr)
        arr1 = [2]
        t = 10**9+7
        for i in range(1,n):
            arr1.append((arr1[i-1]*2)%t)
        total = 0
        for i in range(0,n-1):
            total += arr[i+1]*(arr1[i]-1) - arr[i]*(arr1[n-i-2]-1)
        return (total + t)%t