class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=float('inf')
        max_p=0
        for p in prices:
            if p<minp:
                minp=p
            elif p-minp>max_p:
                max_p=p-minp
        return max_p