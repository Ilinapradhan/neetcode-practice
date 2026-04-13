class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height : return 0
        # l , r = 0 , len(height)-1
        # leftmax , rightmax = height[l] , height[r]
        # res = 0
        # while l<r :
        #     if leftmax < rightmax:
        #         l+=1
        #         leftmax=max(height[l] , leftmax)
        #         res+=height[l]-leftmax
        #     else:
        #         r-=1
        #         rightmax= max(height[r] , rightmax)
        #         res=height[r]-rightmax
        # return res
        if not height: return 0
    
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                # Update leftMax
                leftMax = max(leftMax, height[l])
                # The water trapped is the current peak minus the bar height
                res += leftMax - height[l]
            else:
                r -= 1
                # Update rightMax
                rightMax = max(rightMax, height[r])
                # The water trapped is the current peak minus the bar height
                res += rightMax - height[r]
                
        return res