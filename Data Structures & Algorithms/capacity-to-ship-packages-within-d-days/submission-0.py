class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxwe=0
        for i in weights:
            maxwe+=i
        l=max(weights)
        h=maxwe
        ans=maxwe
        def can_ship(cap):
            curr_we=0
            day=1
            for i in weights:
                if curr_we+i>cap:
                    day=day+1
                    curr_we=i
                else:
                    curr_we=curr_we+i
            return day
        while l<=h:
            mid=l+(h-l)//2
            # current= math.ceil(maxwe/mid)
            if can_ship(mid)<=days:
                ans=mid 
                h=mid-1
            else:
                l=mid+1
        return ans 