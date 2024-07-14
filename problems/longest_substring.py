"""
Есть строка s — нужно найти длину самой длинной подстроки, в которой каждый символ используется только один раз.

если s = "abcabcbb", то ответ будет 3, потому что строка без повторений — это "abc";
если s = "bbbbb", то ответ будет 1, потому что самая длинная подстрока тут будет из одного символа;
если s = "pwwkew", то ответ будет 3, потому что тут две самые одинаково длинные подстроки — "wke" и "kew", в которых по 3 символа.

{
    "b": 1
    "c": 1
    "a": 1
}
max([3, 3, 3, 3, 1]) --> 3
"""

"""
Approach to look for all the occurrences of word in string
s = "Привет, мир! Мир - прекрасен"
substring = 'мир'
indices = []
index = -1  # начинаем поиск с начала строки
 
while True:
    # находим следующее вхождение подстроки
    index = s.find(substring, index + 1)
 
    # если вхождение не найдено, выходим из цикла
    if index == -1:
        break
 
    # добавляем индекс в список
    indices.append(index)
 
print(indices)  # [8, 13]
"""