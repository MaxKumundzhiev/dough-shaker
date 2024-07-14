"""
Есть массив со словами, в котором есть хотя бы одно слово. 
Надо найти максимально длинное общее начало каждого слова. 

Если такого нет — вывести пустую строку.

Пример: у нас есть массив ['дом', 'домен', 'домра', 'доширак']. Общее начало каждого слова — 'до'.
"""


# Time O(n) | Space O(1)
def foo(words: list[str]):
    counter = 0
    for characters in zip(*words):
        match = True if len(set(characters)) == 1 else False
        if match:
            counter += 1
        else:
            return words[0][:counter+1]
    return words[0]

words = ['дом', 'дом', 'домра', 'доширак']
print(foo(words=words))