# Recursive Call of grid traveler
def grid_traveler(m, n):
    if m == 1 and n == 1:  # Base case
        return 1
    if m == 0 or n == 0:  # Base case
        return 0

    return grid_traveler(m-1, n) + grid_traveler(m, n-1)  # Recursive case


# Memoization version
def grid_traveler_memo(m, n, memo={}):
    if f"{m},{n}" in memo:  # If args combination is in memo
        return memo[f"{m},{n}"]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[f"{m},{n}"] = grid_traveler_memo(m-1, n, memo) + grid_traveler_memo(m, n-1, memo)
    return memo[f"{m},{n}"]  # Remember to add memo in your recursive calls!


print(grid_traveler_memo(2, 3))
print(grid_traveler_memo(3, 3))
print(grid_traveler_memo(18, 18))

