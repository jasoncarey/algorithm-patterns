# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram

# TC: O(n)
# SC: O(26) -> O(1)

# Handling unicode:
#   - normalization (NFC)
#   - casefold, more aggressive than lower()
#   s = unicodedata.normalize('NFC', s).casefold()

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        
        for c in s:
            s_map[c] += 1
        for c in t:
            s_map[c] -= 1
        
        for count in s_map.values():
            if count != 0:
                return False
        return True

# Edge cases
solution = Solution()
print(solution.isAnagram("", ""))  # True
print(solution.isAnagram("a", "ab"))  # False
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))  # False
