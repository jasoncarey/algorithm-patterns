## Usage

- backtracking
- depth-first search

## Monotonic Stack
- maintains elements in increasing or decreasing order
- useful for problems requiring us to find the `next smaller` or `next larget` element

```python
# Monotonically increasing stack
stack = []
for element in array:
    while stack and stack[-1] > element:
        stack.pop()
    stack.append(element)

# Monotonically decreasing stack
stack = []
for element in array:
    while stack and stack[-1] < element:
        stack.pop()
    stack.append(element)
```

- note that we can use this approach but store an index instead of the actual value in the monotonic stack

