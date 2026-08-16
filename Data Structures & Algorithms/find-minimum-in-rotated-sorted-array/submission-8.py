class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float('inf')        
        l, r = 0, len(nums) - 1

        if nums[-1] > nums[0] or len(nums) == 1:
            return nums[0]

        while l < r:
            mid  =  (l + r) // 2
            result = min(result, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]