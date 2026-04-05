from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
    
    # Step 2: Use a heap to keep track of top k - O(n log k)
    # We store (-frequency, value) or use nlargest
        return heapq.nlargest(k, count.keys(), key=count.get)
        