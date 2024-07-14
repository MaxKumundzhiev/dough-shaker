"""
В переменной X лежит какое-то целое число
Задача — проверить, является ли это число палиндромом.
"""

# Time O(n/2) | Space O(1)
def foo(digit: int) -> bool:
    digit = str(digit)

    if len(digit) == 0:
        return False
    
    if len(digit) == 1:
        return True

    length = (len(digit) // 2) + 1

    for idx in range(length):
        if digit[idx] != digit[~idx]:
            return False
    return True


"""
121 True
1230321 True
1230021 False
print(foo(digit="1230021"))
"""


"""
Тоже самое только без строк (через mod 10)
-121, 121
"""

