"""
Assume there is an input array of int element. 
You need to return all the permutations (2 digits) of the array.
"""

input = [1, 2, 3]
# what should be returned
# (1, 2), (1, 3), (2, 3)

pairs = []
total_length = len(input)

for outer_idx in range(total_length):
    for inner_idx in range(outer_idx+1, total_length):
        pairs.append((input[outer_idx], input[inner_idx]))

print(pairs)