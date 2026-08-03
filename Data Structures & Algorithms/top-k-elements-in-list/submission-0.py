class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for n in nums:
            count[n] = count.get(n, 0) + 1


        while k > 0:
            largest = count[list(count.keys())[-1]]
            key = list(count.keys())[-1]

            for i, value in count.items():
                if value > largest:
                    largest = value
                    key = i

            result.insert(0, key)
            count.pop(key)
            k -= 1

        
        return result