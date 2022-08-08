# Recursive call
def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        rem = target_sum - num
        rem_result = how_sum(rem, numbers)
        if rem_result is not None:
            rem_result.append(num)  # Important Note: list.append() DOES NOT RETURN ANYTHING, it simply adds to the list
            return rem_result       # Do not do a = a.append(num) or return a.append(num) because doesn't return

    return None


# Memoization version
def how_sum_memo(target_sum, numbers, memo={}):
    if target_sum in memo:  # If target sum stored in memo dictionary
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        rem = target_sum - num
        rem_result = how_sum_memo(rem, numbers, memo)
        if rem_result is not None:
            rem_result.append(num)
            memo[target_sum] = rem_result  # Adding to memo
            return rem_result

    memo[target_sum] = None # Adding to memo
    return None


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum_memo(300, [7, 14]))


