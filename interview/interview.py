# take a list of words and an integer, return up to nth element of list
# take(["apple", "pear", "lemon", "orange"], 2)
# ["apple", "pear"]
# if int bigger than list return original list

# take(["apple", "pear", "lemon", "orange"], 5)
# ["apple", "pear", "lemon", "orange", "apple"]

# take(["apple", "pear", "lemon", "orange"], 6)
# ["apple", "pear", "lemon", "orange", "lemon", "pear"]


def take(input_list, n):
    return_list = []

    # for i, word in enumerate(input_list):
    # if i > n - 1:
    #    return return_list
    # return_list.append(word)

    len_input = len(input_list)
    i = 0
    j = 0
    reverse = False
    while i < n:
        print(i, j)
        return_list.append(input_list[j])

        if j >= len_input - 1:
            reverse = True
        if j == 0:
            reverse = False

        i += 1

        if reverse:
            j -= 1
        else:
            j += 1

    return return_list


print(take(["apple", "pear", "lemon", "orange"], 6))
