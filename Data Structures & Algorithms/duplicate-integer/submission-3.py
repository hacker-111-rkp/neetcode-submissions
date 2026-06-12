class Solution:
    def hasDuplicate(self, nums):
        a=set(nums)
        if len(a)==len(nums):
            return False
        return True
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))