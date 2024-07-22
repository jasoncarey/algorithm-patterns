# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams

# TC: O(n.klog(k)) -> O(nlogk) 
# SC: O(n.k) -> O(n)
# where k is the average word length

from typing import List

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            ordered_word_list = sorted(word)
            ordered_word = ''.join(ordered_word_list) # turn list into a string (hashable type)
            if ordered_word not in d:
                d[ordered_word] = [word]
            else:
                d[ordered_word].append(word)
        
        return list(d.values())

solution = Solution()
print(solution.group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.group_anagrams([""]))
print(solution.group_anagrams(["a"]))
print(solution.group_anagrams(["ddddddddddg","dgggggggggg"]))