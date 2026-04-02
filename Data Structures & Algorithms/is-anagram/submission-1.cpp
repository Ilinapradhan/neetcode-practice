class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }
        int counter[26] = {0}; 
        for (int i ; i<s.length() ; i++){
            counter[s[i]-'a']++;
            counter[t[i]-'a']--;
        }
        for (int j=0 ; j<26 ; j++){
            if (counter[j] !=0){
                return false ;
               
            }
            
        }
        return true;
    }
};
