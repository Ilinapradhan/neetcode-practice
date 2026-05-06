class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi=max(piles)
        l=1
        r=hi
        while l<=hi:
            mid = l+ (hi-l)//2
            time=0
            for p in piles:
                time=time+math.ceil(p/mid)
            if time<=h:
                r=mid 
                hi=mid-1
            else:
                l=mid+1
        return r
