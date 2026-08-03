class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # anagram => count,index
        count = 0
        result = []

        for i,s in enumerate(strs):
            sorted_s = ''.join(sorted(s))
            if (sorted_s not in anagrams):
                anagrams[sorted_s] = count
                result.append([])
                count += 1

            result[anagrams[sorted_s]].append(s)

        return result