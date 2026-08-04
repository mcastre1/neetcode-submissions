import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if len(cleaned_string) % 2 == 0: 
            half = int(len(cleaned_string)/2)
            left = cleaned_string[:half]
            right = cleaned_string[half:]
            print(left)
            print(right)
            return left[::-1] == right
        else:
            print(cleaned_string)
            half = int(len(cleaned_string)/2)
            left = cleaned_string[:half]
            right = cleaned_string[half+1:]

            return left[::-1] == right
