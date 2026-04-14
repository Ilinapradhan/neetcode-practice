class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        r=0
        l=0
        res=0
        while r<len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            res=max(res , r-l+1)
            r+=1
        return res