from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    
    # # Step 2: Use a heap to keep track of top k - O(n log k)
    # # We store (-frequency, value) or use nlargest
    #     return heapq.nlargest(k, count.keys(), key=count.get)
        counter={}
        freq=[[] for i in range(len(nums)+1)]
        for i in nums :
            counter[i]=1 + counter.get(i , 0)
        for n , c in counter.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1 , 0 , -1):
            for j in freq[i]:
                if len(res)<k:
                    res.append(j)
        return res



        