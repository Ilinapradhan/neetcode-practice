class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        count1 , count2 , can1 , can2 = 0 , 0 , None , None
        for n in nums:
            
            if n == can1:
                count1+=1
            elif n==can2:
                count2+=1
            elif count1==0:
                can1=n 
                count1=1
            elif count2==0:
                can2=n
                count2=1
            else :
                count1 -=1
                count2-=1
        res=[]
        for can in [can1 , can2]:
            if nums.count(can) > len(nums)//3 :
                res.append(can)
        return list(set(res))