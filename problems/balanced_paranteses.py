"""
give sequence of parantesess of type `()`. Verify if sequence is balanced.
"""

from typing import List


def foo(sequence: List[str]) -> bool:
    stack = []  # follows LIFO concept
    stack_is_empty = True

    opening = "("

    for parentheses in sequence:
        # parentheses is openining
        if parentheses == opening:
            stack.append(parentheses)
            stack_is_empty = False
        # parentheses is closing
        else:
            if stack_is_empty is True:
                return False
            else:
                del stack[-1]
                stack_is_empty = True if len(stack) == 0 else False
    
    return True if stack_is_empty is True else False


assert foo(sequence="(())") == True
assert foo(sequence="())") == False