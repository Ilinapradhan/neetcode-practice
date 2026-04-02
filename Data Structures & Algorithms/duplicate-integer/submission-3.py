class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        #         break
        # return False
        unique = set()
        for x in nums:
            if x in unique:
                return True 
                break
            unique.add(x)
        return False