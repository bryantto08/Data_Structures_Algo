# Recursive call of can sum function
def can_sum(target_sum, numbers):
    if target_sum == 0:  # If values of array equal the target num
        return True
    if target_sum < 0:  # If those specific order of values does not equal the target num
        return False
    for num in numbers:
        if can_sum(target_sum - num, numbers):
            return True
    return False


def can_sum_memo(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:  # If values of array equal the target num
        return True
    if target_sum < 0:  # If those specific order of values does not equal the target num
        return False
    for num in numbers:
        rem = target_sum - num
        if can_sum_memo(rem, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


print(can_sum_memo(7, [2, 3]))
print(can_sum_memo(7, [5, 3, 4, 7]))
print(can_sum_memo(7, [2, 4]))
print(can_sum_memo(8, [2, 3, 5]))
print(can_sum_memo(300, [7, 14]))
