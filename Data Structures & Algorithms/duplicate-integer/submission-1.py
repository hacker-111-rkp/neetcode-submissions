class Solution:
    def hasDuplicate(self,nums):
        count=0
        hashmap={}
        for i,number in enumerate(nums):
            if number in hashmap:
                return True
            else :
                hashmap[number]=i
        return False
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))