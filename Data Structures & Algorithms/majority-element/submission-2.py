class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[int(len(nums)/2)]

        # for i in nums:
        #     count =0 
        #     if count==0:
        #         res=i
        #     count += (1 if res==i else -1)
        # return res

        res, count = 0, 0
    
        for n in nums:
            # If count hits 0, we pick a new 'candidate'
            if count == 0:
                res = n
            
            # If the current number matches our candidate, add a vote
            # Otherwise, subtract a vote (the "argument" that removes both)
            count += (1 if n == res else -1)
            
        return res