class Solution:
    def search(self, nums: List[int], target: int) -> int:
        window = (0, len(nums))
        found = False

        while not found:
            if window[1] - window[0] <= 1:
                found = True
            
            mid = int((window[1] - window[0]) / 2)
            
            if target >= nums[window[0] + mid]:
                window = (window[0] + mid, window[1])
            else:
                window = (window[0], window[1] - mid)

        if nums[window[0]] == target:
            return window[0]
        else:
            return -1
            
