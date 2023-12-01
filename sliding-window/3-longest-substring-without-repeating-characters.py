# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# TC: O(n)
# SC: O(n)

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        # Substring -> Sliding Window
        # Longest -> Dynamic
        # Repeating characters -> aux. data structure required
        # No repeat allowed -> use a set()

        if not s: return 0

        start = 0
        longest = 1
        curr = 1
        freq = set(s[start])

        for end in range(1, len(s)):
            while s[end] in freq:
                freq.remove(s[start])
                start += 1
                curr -= 1
            
            freq.add(s[end])
            curr += 1
            longest = max(longest, curr)

        return longest