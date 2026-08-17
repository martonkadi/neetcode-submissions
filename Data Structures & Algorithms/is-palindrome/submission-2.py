class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        if not s:
            return True
        start = s[0]
        end = s[-1]

        for i in range(len(s)):
            if start != end:
                return False
            start = s[i]
            end = s[len(s)-i-1]
        return True