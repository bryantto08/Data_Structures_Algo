# Find the Longest substring length with K distinct characters

# Dynamic Window Sliding with Dictionary

def longest_substring(s, k):
    hashmap = {}
    max_value = 0
    curr_value = 0
    window_start = 0

    for i in range(len(s)):  # O(n)
        if s[i]in hashmap:  # If the same letter is in hashmap, add one
            hashmap[s[i]] += 1
        else:  # If different letter, create new key
            hashmap[s[i]] = 1

        while len(hashmap) > k:  # If there are more distinct keys than k
            hashmap[s[window_start]] -= 1  # Subtract 1 from the value of the key of window_start
            if hashmap[s[window_start]] == 0:  # If no more values, delete key
                del hashmap[s[window_start]]
            window_start += 1  # Increment the start of the Sliding Window
        max_value = max(max_value, i - window_start + 1)

    return max_value

a = "aaahhibc"
print(longest_substring(a,2))

