class Solution:
    def mySqrt(self, x: int) -> int:

        # l = 0
        # r = x//2

        # while l<=r:
        #     mid = l + (r-l)//2
        #     num = mid *mid
        #     if num <= num:
        #         low = mid +1
            
        if x<2:
            return x
        l , r = 2 , x//2
        ans =1 
        while l<=r:
            mid = l+(r-l)//2
            num=mid*mid
            if num==x:
                return mid
            elif num < x :
                ans = mid 
                l=mid +1
            else :
                r = mid -1 
        return ans