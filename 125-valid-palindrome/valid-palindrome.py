class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_s = "".join(ch.lower() for ch in s if ch.isalnum())
        l, r = 0, len(l_s) - 1

        while l < r:
            if l_s[l] != l_s[r]:
                return False
            l += 1
            r -= 1

        return True