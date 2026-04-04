class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # def heapify(n, i):
        #     largest = i
        #     l, r = 2 * i + 1, 2 * i + 2
        #     if l < n and nums[l] > nums[largest]: largest = l
        #     if r < n and nums[r] > nums[largest]: largest = r
        #     if largest != i:
        #         nums[i], nums[largest] = nums[largest], nums[i]
        #         heapify(n, largest)

        # n = len(nums)
        # # Build Max Heap
        # for i in range(n // 2 - 1, -1, -1):
        #     heapify(n, i)
        # # Extract elements
        # for i in range(n - 1, 0, -1):
        #     nums[i], nums[0] = nums[0], nums[i]
        #     heapify(i, 0)
        # # return nums

        low , mid , high = 0 , 0 , len(nums)-1
        while mid <= high :
            if nums[mid]==0:
                nums[mid] , nums[low] = nums[low] , nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else :
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high-=1
                
        