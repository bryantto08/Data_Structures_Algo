# Tabulation
def fib_tab(num):
    num_list = [0] * (num + 1)
    num_list[1] = 1
    for i in range(num):
        if i == num-1:  # Don't want to add to an index that doesn't exist
            num_list[i+1] += num_list[i]
        else:
            num_list[i+1] += num_list[i]
            num_list[i+2] += num_list[i]

    return num_list[num]


print(fib_tab(6))
print(fib_tab(7))
print(fib_tab(8))
print(fib_tab(50))
