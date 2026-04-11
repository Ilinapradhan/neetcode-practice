class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=[]
        l=min(len(word1) , len(word2))
        for i in range(l):
            s.append(word1[i])
            s.append(word2[i])
        
        s.append(word1[l::])
        
        s.append(word2[l::])
        
        return "".join(s)