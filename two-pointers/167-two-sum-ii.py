# 167. Two Sum II - Input Array is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# Medium
# Two Poiners

# There is *exactly* one solution


def two_sum(numbers, target):

    i, j = 0, len(numbers) - 1

    while i < j:
        curr_sum = numbers[i] + numbers[j]

        if curr_sum == target:
            return [i + 1, j + 1]
        elif curr_sum < target:
            i += 1
        else:
            j -= 1


# --------------------------------- #

print("Expected: [1, 2]")
print("Got: ", two_sum([2, 7, 11, 15], 9))

print("Expected: [1, 3]")
print("Got: ", two_sum([2, 3, 4], 6))

print("Expected: [1, 2]")
print("Got: ", two_sum([-1, 0], -1))
