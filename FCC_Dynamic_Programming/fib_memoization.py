# Recursive function of the fib sequence
def fib(n):  # 1, 1, 2, 3, 5, 8, 13, 21
    if n <= 2:  # If index n == 1 (1,2)
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # Think of recursive call as a stack


# Memoization
# Keys would be arguments to function, values would be the return value
def fib_memo(n, memo={}):  # 1, 1, 2, 3, 5, 8, 13, 21
    # Is argument in memo
    if n in memo:
        return memo[n]
    if n <= 2:  # If index n == 1 (1,2)
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)  # Passing in the same memo into recursive call
        return memo[n]  # Think of recursive call as a stack


print(fib_memo(7))
print(fib_memo(8))
print(fib_memo(9))
print(fib_memo(50))
