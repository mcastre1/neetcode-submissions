class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i, n in enumerate(nums):
            temp_nums = nums.copy()
            temp_nums.pop(i)
            result = 1
            for n in temp_nums:
                result = result * n

            products.append(result)


        return products