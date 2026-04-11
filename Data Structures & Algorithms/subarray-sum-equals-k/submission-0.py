class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0 
        cur_sum=0
        prefix_sum={0:1}
        for i in nums:
            cur_sum+=i
            diff=cur_sum - k
            if diff in prefix_sum :
                count+= prefix_sum[diff]
            prefix_sum[cur_sum]=prefix_sum.get(cur_sum , 0)+1
        
        return count