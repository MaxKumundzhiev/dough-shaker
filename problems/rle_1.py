"""
Дана трока вида содержазая эдементы A-Z (e.g. AAABCCDEEFGG)
Выведи сокразенную строку, где каждый символ повторяется 1 раз
"""


def unique_rle(string: str) -> str:
    return "".join(sorted(set(string)))


def unique_rle_with_counter(string: str) -> str:
    """idea to have hash with unique elements from input"""
    hash = {}
    for idx in range(len(string)):
        current = string[idx]
        if current not in hash:
            hash[current] = True
        else:
            continue
    return "".join(hash.keys())

def rle_with_last_element(string: str) -> str:
    "AAAAABBB"

    answer = []
    last_seen = string[0]

    for idx in range(1, len(string)):
       if string[idx] != last_seen:
           answer.append(last_seen)
           last_seen = string[idx]

    answer.append(last_seen)
    return "".join(answer)


if __name__ == "__main__":
    input = "AAAAABBBCASFSA"
    print(unique_rle(string=input))
    print(unique_rle_with_counter(string=input))
    print(rle_with_last_element(string=input))