# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # low = 1
        # high = n
        
        # while low <= high:
        #     # Calculate the middle point
        #     mid = low + (high - low) // 2
            
        #     # Call the API
        #     res = guess(mid)
            
        #     if res == 0:
        #         return mid  # Found it!
        #     elif res == -1:
        #         # Our guess was too high, look at the left half
        #         high = mid - 1
        #     else:
        #         # Our guess was too low, look at the right half
        #         low = mid + 1
                
        # return -1
        l,r=0,n
        while l<=r:
            mid = l+(r-l)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res == -1:
                r=mid-1
            else:
                l=mid+1
        return -1 