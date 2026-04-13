class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r =0 , len(heights)-1
        cur_vol=0
        max_vol = 0
        while l<r:
            cur_vol = (r-l)*min(heights[l] , heights[r])
            max_vol= max(cur_vol , max_vol)
            if heights[l]>heights[r]:
                r-=1
            else :
                l+=1
        return max_vol