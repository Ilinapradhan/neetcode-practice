class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def reversek(l , r ):
            while l<r:
                nums[l] , nums[r]= nums[r] , nums[l]
                l+=1
                r-=1
        reversek(0 , n-1)
        reversek(0 , k-1)
        reversek(k, n-1)
        return nums