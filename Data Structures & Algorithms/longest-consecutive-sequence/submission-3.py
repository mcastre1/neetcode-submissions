class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = list(set(sorted(nums)))
        ns = {}
        starts = {}
        
        for i,n in enumerate(nums):
            ns[n] = i

        for i,n in enumerate(nums):
            if n - 1 not in ns:
                starts[n] = i

        sequences = []

        for n in nums:
            if n in starts:
                temp = 1
                while True:
                    if n + temp in ns:
                        temp += 1
                    else:
                        sequences.append(temp)
                        break

        return sorted(sequences)[-1]
                    

                    



