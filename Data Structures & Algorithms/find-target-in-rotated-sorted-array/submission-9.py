class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        shift = l

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            real_mid = (mid + shift) % len(nums)

            if nums[real_mid] == target:
                return real_mid

            if nums[real_mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1