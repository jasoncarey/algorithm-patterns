# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

# TC: O(n)
# SC: O(n)

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        # Substring -> Sliding window
        # Permutation -> Aux. data structure -> Hash map
        # s1 fixed length -> Fixed window
        # s1 freq == s2 window freq

        if not s1 or not s2: return False
        start = 0
        freq_s1, freq_s2 = {}, {}
        freq_s2[s2[start]] = 1

        for letter in s1:
            freq_s1[letter] = freq_s1.get(letter, 0) + 1

        for end in range(1, len(s2)):
            if freq_s2 == freq_s1: return True
            freq_s2[s2[end]] = freq_s2.get(s2[end], 0) + 1
            
            if end - start != len(s1): continue
            
            if freq_s2[s2[start]] == 1:
                freq_s2.pop(s2[start])
            else:
                freq_s2[s2[start]] -= 1
            start += 1

        return freq_s1 == freq_s2