class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]

        # for i in nums:
        #     count =0 
        #     if count==0:
        #         res=i
        #     count += (1 if res==i else -1)
        # return res