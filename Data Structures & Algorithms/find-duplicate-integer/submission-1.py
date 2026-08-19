class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        nums = sorted(nums)
        
        for i, v in enumerate(nums):
            if v < (i + 1):
                return v
            