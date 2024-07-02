
# array = [-1, 10, 9, 0]
# array = ["bed", "bat", "house", "door"]
# array = ["aabasdas", "aassa", "asfasfsasaf", "abc"]

from typing import List


def count(word):
  return word.count("b")

# Best O(n)
# Average O(n*log(n))
# Worst O(n*log(n))
# print(sorted(array, key=count, reverse=True))

# ord - numer representation of letter
# table ASCII
# for letter in array[0]:
#   print(ord(letter))

# for letter in array[1]:
#   print(ord(letter))


class String:
  # Time O(n + m)
  # Space O(n)
  @staticmethod
  def capitalize(word: str):
    """Capitalize first letter of word."""
    
    difference_between_upper_and_lower = 32
    upper_case_range = range(65,91)
    
    if len(word) == 0:
      return word
  
    letter = ord(word[0])
  
    # edge case if letter already capitalized
    if letter in upper_case_range:
      return word
    # edge case if letter is not capitalized
    else:
      letter -= difference_between_upper_and_lower
      word = chr(letter) + word[1:]
  
    return word 

  # Time O(n + m)
  @staticmethod
  def casefold(word: str):
    """Lower first letter of word."""
    
    exclude_alph = "{}/\,;:.!?'[]"
    lowercase_range = range(97, 123)
    difference = 32
    
    if len(word) == 0:
      return word

    letter = word[0]
    numeric = ord(letter)

    if numeric in lowercase_range or letter in exclude_alph:
      return word
      
    numeric += difference
    letter = chr(numeric)
    word = letter + word[1:]
    
    return word

  # Time O(n) | Space O(n)
  @staticmethod
  def center(word, length, character=" ") -> str:
    """Adds leading and trailing symbols."""
    addition = length*character
    return addition + word + addition
    
    # # array Space O(N)
    # result = []
    
    # result.append(character*length)
    # result.append(word)
    # result.append(character*length)
    # # join() Time O(N) 
    # return "".join(result)
  
  @staticmethod
  def count(word, character = None) -> int | None:
    """
    Returns the number of times a specified value occurs in a string
    """
    counter = 0

    if len(word) == 0 or character is None:
      return None
          
    for letter in word:
      if letter == character:
        counter += 1
    return counter
    
  # Time O(1) | Space O(1)
  @staticmethod
  def endswith(word, character = None) -> bool:
    """Returns true if the string ends with the specified value"""

    # if empty word or character is None
    if len(word) == 0 or character is None:
      return False
    
    last = word[-1]
    return last == character

  # Time O(1) | Space O(1)
  @staticmethod
  def startwith(word, character = None) -> bool:
    """Returns true if the string starts with the specified value"""
    if len(word) == 0 or character is None:
      return False

    first = word[0]
    return first == character

  # Time O(n) | Space O(1)
  # (n == lenght word // lenght look up)
  @staticmethod
  def find(word: str, to_look_up: str):
    """
    Returns subsctring index slice if found, otherwise -1
    """
    window = len(to_look_up)
    
    if len(word) == 0 or window == 0 or window > len(word):
      return -1
      
    for idx in range(0, len(word)-window+1, 1):
      substring = word[idx:idx+window]
      if substring == to_look_up:
        return f"{idx}:{idx+window-1}"
      else:
        continue
    return -1

  # Time O(n) | Space O(1)
  @staticmethod
  def index(word: str, character: str) -> int:
    """
    Returns index of 1st occurrence of character, otherwise -1
    """    
    if len(word) == 0 or len(character) != 1:
      return -1
    for idx, letter in enumerate(word):
      if letter == character:
        return idx
    return -1


  # Python implementation of "join"
  # Time O(n) | Space O(n)
  # Ours implementation of "join"
  # Time O(n^2) | Space O(n)
  @staticmethod
  def join(words: List[str]) -> str:
    """
    Returns joined string of words.
    """
    
    result = ""
    for word in words:
      result += word
    return result
  
  # Time O(n) | Space O(1)
  @staticmethod
  def replace(
    words: List[str], replace: str, word: str
  ) -> str:
    """
    Returns a string where a specified value is replaced with a 
    specified value
    """

    # edge case: if replace empty
    if replace is None:
      return words

    # main logic
    for idx, word_ in enumerate(words):
      if word_ == replace:
        words[idx] = word
        return words
    return -1

  # Time O(n*m)
  # where n lenght of the string
  # where m sum of lenght of all words
  @staticmethod
  def split(words, separator, maxsplit):
    """
    Splits the string at the specified separator, and returns a list
    """

    """
    iasfsafsa live lonely live
             |
             |
    [i, live, lonely, live]
    """

    # "__bat___look"
    
    idx, iterable = 0, []
    
    while idx < len(words):
      if words[idx] == separator:
        idx += 1
      else:
        idx_ = idx
        while words[idx_] != separator:
          if idx_ + 1 >= len(words):
            iterable.append(words[idx:idx_+1])
            return iterable
          else:
            idx_ += 1
        
        iterable.append(words[idx:idx_])
        idx = idx_
    
    return iterable
    #Time O(n) | Space O(1)
  @staticmethod
  def strip(word: str, characters: str = None):
    """Returns a trimmed version of the string
    By default strip deletes all the backspaces from left and right.
    """
    
    if len(word) == 0:
      return word
    if len(characters) == 0:
      characters = " "
    l, r = 0, len(word)-1
    
    while True:
      left, right = word[l], word[r]
      if left == characters:
        l += 1
      elif right == characters:
        r -= 1
      else:
        return word[l:r+1]
    



print(String().casefold(word="Aasfsa"))
print(String().center(word="aa", length=2, character="*"))
print(String().count(word="aaa", character="b"))
print(String().startwith(word="abbc", character="s"))
print(String().find(word="aaa", to_look_up="a"))
print(String().index(word="aaab", character="aa"))
print(
  String().replace(
    words=["i", "bat", "door"], replace="bat", word="man"
  )
)
print(String().split(words="       bat       look    ", separator=" ", maxsplit = None))

#print("  aa aba ab      ".strip(b))

print(String().strip(word="   a  ##aa#  a ", characters=""))