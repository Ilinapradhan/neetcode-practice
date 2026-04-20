class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or not t :
            return ""

        counts , countt = {} , {}
        for c in t:
            countt[c]=1+ countt.get(c , 0 )
        
        need=len(countt)
        have=0
        res , reslen = [-1 ,-1] , float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            counts[c]=1+counts.get(c,0)
            if c in countt and countt[c]==counts[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    reslen=r-l+1
                    res=[l,r]
                counts[s[l]]-=1
                if s[l] in countt and countt[s[l]]> counts[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!= float("infinity") else ""