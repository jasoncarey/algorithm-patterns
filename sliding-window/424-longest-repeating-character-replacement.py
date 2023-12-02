# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Substring -> sliding window
        # Longest -> dynamic
        # Frequency -> aux data structure
        # K operations -> hash map

        if not s: return 0

        start = 0
        max_char = 1
        freq = {}

        freq[s[start]] = 1

        for end in range(1, len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_char = max(max_char, freq[s[end]])
            if end - start + 1 > max_char + k:
                freq[s[start]] = freq[s[start]] - 1
                start += 1  

        if len(s) < max_char + k: return len(s) 
        else: return max_char + k
