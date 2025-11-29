from countStepsMemoization import count_steps

memo = {}
steps = [1, 3, 5]
print(count_steps(20,steps, memo))
assert(20 - step in memo for step in steps)
assert(20 in memo)