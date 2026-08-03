class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "null"

        shifted_words = []
        for s in strs:
            shifted_chars = []
            for ch in s:
                new_code = (ord(ch) + 3) % 256
                shifted_chars.append(chr(new_code))

            shifted_words.append(''.join(shifted_chars))

        return '!leet#'.join(shifted_words)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]

        if s == "null":
            return []

        if not s:
            return []

        words = s.split('!leet#')
        shifted_words = []

        for s in words:
            shifted_chars = []
            for ch in s:
                new_code = (ord(ch) - 3) % 256
                shifted_chars.append(chr(new_code))
            
            shifted_words.append(''.join(shifted_chars))
            
        return shifted_words