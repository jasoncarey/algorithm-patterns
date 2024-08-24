"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

Medium

TC: O(n)
SC: O(n)
"""


def eval_rpn(tokens) -> int:

    stack = []
    operators = ["+", "-", "*", "/"]

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            operand1, operand2 = stack.pop(), stack.pop()

            match (token):
                case "+":
                    res = operand2 + operand1
                case "-":
                    res = operand2 - operand1
                case "*":
                    res = operand2 * operand1
                case "/":
                    res = int(operand2 / operand1)

            stack.append(res)

    return stack[-1]


# --------------------------------- #
print("Expected: 9, Got: ", eval_rpn(["2", "1", "+", "3", "*"]))
print("Expected: 6, Got: ", eval_rpn(["4", "13", "5", "/", "+"]))
print(
    "Expected: 22, Got: ",
    eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
)
