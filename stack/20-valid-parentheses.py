"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses

Easy

TC: O(n)
SC: O(n)
"""


def is_valid(s: str) -> bool:

    parentheses = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for c in s:
        if c in parentheses:
            stack.append(c)
        else:
            if not stack:
                return False
            open_bracket = stack.pop()
            if parentheses[open_bracket] != c:
                return False

    return not stack


# --------------------------------- #

print("Expected: True, Got: ", is_valid("()[]{}"))
print("Expected: False, Got: ", is_valid("([]{)}"))
