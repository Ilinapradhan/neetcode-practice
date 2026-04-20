class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores indices
        
        for i, n in enumerate(nums):
            # 1. Pop elements from the back that are smaller than current number
            while q and nums[q[-1]] < n:
                q.pop()
            
            q.append(i)
            
            # 2. Remove the front element if it's outside the window
            if q[0] == i - k:
                q.popleft()
                
            # 3. If window is fully formed, the front of queue is the max
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res