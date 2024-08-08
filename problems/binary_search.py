

from typing import List, Union


def binary_search(sequence: List[int], target: int) -> Union[int]:
    low = 0
    high = len(sequence) - 1

    while low <= high:
        middle = low + high
        guess = sequence[middle]

        if guess == target:
            return middle
        elif guess > target:
            high = middle - 1
        else:
            low = middle + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 5))



def removeOuterParentheses(s: str) -> str:
    ans = []
    count = 0

    for char in s:
        if char == ')':
            count -= 1
        if count != 0:
            ans.append(char)
        if char == '(':
            count += 1

    return ''.join(ans)


s = "(()())(())"
print(removeOuterParentheses(s=s))