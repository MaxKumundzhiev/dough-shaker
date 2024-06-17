"""
Дана трока вида содержазая эдементы A-Z (e.g. AAABCCDEEFGG)
Выведи строку вида 3AB2CD2EF2G
"""

def pack(letter: str, counter: int) -> str:
    if counter == 1:
        return letter
    else:
        return f'{counter}{letter}'

def rle(string: str) -> str:
    answer = []
    left, right, counter = 0, 1, 1

    while True:
        current = string[left]
        try:
            last = string[right]
        except IndexError:
            answer.append(pack(letter=current, counter=counter))
            return "".join(answer)
        if current == last:
            right += 1
            counter += 1
        else:
            answer.append(pack(letter=current, counter=counter))
            left = right
            right = left + 1
            counter = 1

"""
AABBC  it = 3
"""

if __name__ == "__main__":
    input = "AABBCDEEEE"
    expected = "2A2BCD4E"

    answer = rle(string=input)
    print(answer)
    print(expected)

