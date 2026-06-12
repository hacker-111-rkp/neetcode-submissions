class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_type={}
        if len(s)!=len(t):
            return False
        for x in s :
            hash_type[x]=hash_type.get(x,0)+1  
        for x in t:
            if x not in hash_type:
                return False
            hash_type[x]-=1
            if hash_type[x]<0:
                return False
        return True