# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome
# Two Pointers


def is_palindrome(s: str) -> bool:

    i, j = 0, len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True


# --------------------------------- #

print("Expected: True")
print("Got: ", is_palindrome("A man, a plan, a canal: Panama"))

print("Expected: False")
print("Got: ", is_palindrome("race a car"))

print("Expected: True")
print("Got: ", is_palindrome(" "))

print("Expected: False")
print("Got: ", is_palindrome("0P"))
