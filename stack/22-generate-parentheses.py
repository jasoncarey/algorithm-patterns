"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Medium
Backtracking

Approach:
- We can add an opening bracket when the number of opening brackets < n
- We can add a closing bracket when the number of opening brackets > number of closing brackets

TC: O(2^n) -> O(n)
SC: O(n)
"""


def generate_parentheses(n: int):

    res = []

    def backtrack(curr, num_opening, num_closing):
        if num_opening == num_closing == n:
            res.append("".join(curr))
            return

        if num_closing < num_opening:
            curr.append(")")
            backtrack(curr, num_opening, num_closing + 1)
            curr.pop()

        if num_opening < n:
            curr.append("(")
            backtrack(curr, num_opening + 1, num_closing)
            curr.pop()

    backtrack(["("], 1, 0)

    return res
