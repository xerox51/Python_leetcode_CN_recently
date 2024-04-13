class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if len(cont)==1:
            return [cont[0],1]
        cont = cont[::-1]
        ans = [cont[0] * cont[1] + 1, cont[0]]
        for i in cont[2:]:
            ans[0], ans[1] = ans[0] * i + ans[1], ans[0]
        return ans