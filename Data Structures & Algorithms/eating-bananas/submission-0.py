import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid = 0

        while low < high:
            mid = (low + high) // 2
            takenHours = self.calculateHours(piles, mid)

            if takenHours > h:
                low = mid + 1
            else:
                high = mid

        return low
    
    def calculateHours(self, piles: List[int], k: int) -> int:
        takenHours = 0
        for p in piles:
            takenHours += math.ceil(p/k)

        return takenHours
            