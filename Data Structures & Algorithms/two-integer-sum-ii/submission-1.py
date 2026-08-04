class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1

        while True:
            l = numbers[i]
            r = numbers[j]

            if target == (l + r):
                return [i+1, j+1]
            elif (l+r) > target:
                j -= 1
            elif (l+r) < target:
                i += 1