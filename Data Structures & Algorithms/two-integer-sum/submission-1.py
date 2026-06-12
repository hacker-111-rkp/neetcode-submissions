#hash map 
class Solution:
    def twoSum(self,nums,target):
        hashmap={}
        for i,nums in enumerate(nums):
            complement = target - nums   
            if complement in hashmap:
                return [hashmap[complement] , i ]
            
            hashmap[nums] = i

sol = Solution()
a=sol.twoSum([3,4,5,6],7)
print(a)