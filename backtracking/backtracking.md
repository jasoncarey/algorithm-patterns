# Backtracking

- Use brute force to build the solution incrementally
- If the current solution can't lead to a valid solution, go back to try another
- Use when multiple valid solutions are possible for a problem

## General solution:

- Pick a starting point.
- while(Problem is not solved)
  - For each path from the starting point.
    - check if selected path is safe
      - if yes select it
      - make recursive call to rest of the problem
      - undo the current move.
If none of the move works out, return false, NO SOLUTON.

```python
def solution:
  result = []
  def backtrack(path, options):
    if is_solution(path):
      result.append(path[:])
      return
    
    for i in range(len(options)):
      choice = options[i]
      path.append(choice)
      backtrack(path, new_options)
      path.pop()

  backtrack([], initial_options)
  return result
```

```python
# Make a list of lists unqiue
seen = set()
unique_result = []
for combination in result:
    combination.sort()
    t = tuple(combination)
    if t not in seen:
        unique_result.append(combination)
        seen.add(t)
```