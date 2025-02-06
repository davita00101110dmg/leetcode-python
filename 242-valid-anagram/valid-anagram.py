class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        
        if len(s) != len(t):
            return False

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for char in t:
            if hashmap.get(char, 0) > 0:
                hashmap[char] -= 1
            else:
                return False
        return True