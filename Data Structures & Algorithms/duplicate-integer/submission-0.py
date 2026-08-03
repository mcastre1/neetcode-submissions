class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = []
        for n in nums: 
            if n in uniques:
                return True
            uniques.append(n)
        
        return False
            