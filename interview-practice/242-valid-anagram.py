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
    def is_anagram(self, s: str, t: str) -> bool:
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
print(solution.is_anagram("", ""))  # True
print(solution.is_anagram("a", "ab"))  # False
print(solution.is_anagram("anagram", "nagaram"))  # True
print(solution.is_anagram("rat", "car"))  # False
