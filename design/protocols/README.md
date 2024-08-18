resource information taken from: https://www.youtube.com/watch?v=Lddegb2ToNY

## Notion
Duck typing - is another way to achive polymorphism besides Inheritance. Object must have the minimum neccessary attributes/methods a.k.a. (`If it walks like a duck, if it quaks like a duck, it must be a duck`)

# Dynamic / Static typing
- Python is `dynamically` typed language - meaning:
    - types are checked at `runtime`
    - type declaration is not required 

```python
def foo(a, b, c):
    return a + b - c

result = foo(5, 3, 2)
# print(type(result)) --> int

result = foo(5.1, 3, 2)
# print(type(result)) --> float
```

# Dynamic typing a.k.a Duck typing
- `Dynamic typing` is same meaning as `duck typing`
    - Often said: `If it walks like a duck, if it quaks like a duck, it must be a duck`

- Full definition:
```
Duck typing in Python is a programming concept where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
```

- `Dynamic typing` (or `duck typing`) works as:
    - no type declaration required
    - lots of flexibility
    - no type checking except at runtime

```python
class Duck:
    def walk(self):
        ...
    
    def quack(self): 
        ...

duck = Duck()
duck.walk()
duck.quack()
```

# Type hints
Commonly used `mypy`, which is meant to check typings before runtime.

- `Type hints` works as:
    - type declarations are optional
    - Optional static type checking
    - Con not adopt type hints of imported code

# ABCs (Abstract Base Classes)
- ABCs - Abstract Base Classes, which you `can inherit from`, but they `can not be instantiated`. Used to define an interface of how subclasses should look like.

```python
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass  # needs implementation by subclass

animal = Animal()
# TypeError: Can't instantiate abstract class Animal with abstract method walk

# instead what we can do
class Duck(Animal):
    def walk(self):
        ...

duck = Duck()
assert isinstance(duck, Animal)  # <-- True
```

One more example with `animals and eating bread`
```python
from abs import ABCMeta, abstractmethod

class EatsBread(metaclass=ABCMeta):
    @abstctmethod
    def eat_bread(self):
        pass

class Duck(EatsBread):
    def eat_bread(self):
        ...

class Pig(EatsBread):
    def eat_bread(self):
        ...

def feed_bread(animal: EatsBread):
    animal.eat_bread()

### if use as imported code
from animals import EatsBread, feed_bread

class Mees(EatsBread):
    def eat_bread(self):
        ...
    
    def drink_milk(self):
        ...

feed_bread(animal=Mees())  # <- OK
```

Remember, there are 2 major approaches to `inherit`, inclusevly from Abstract Base Classes
1. Explicit inheritance
2. Implicit inheritance

```python
# Explicit inheritance

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

class Dog(Animal):
    def walk(self):
        ...

asser isinstace(Dog(), Animal)
```

```python
# Implicit inheritance

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

class Dog:
    def walk(self):
        ...

Animal.register(Dog)
asser isinstace(Dog(), Animal)
```

Example, when ABCs is not that expected and efficient as we wish
```python
# package animals
class Animal(ABC):
    @abstractmethod
    def walk(self):
        ...

class Dog(Animal):
    def walk(self):
        ...

def walk_animal(animal: Animal):
    animal.walk()

# package llamas
class Llama(ABC):
    @abstractmethod
    def walk(self):
        ...

# working file
from animals import walk_animal
from llamas import Llama

llama = Llama()
walk_animal(animal=llama) # <- not OK

# we can fix it, but is fishy
from animals import Animal, walk_animal
from llamas import Llama

# Explicitly make Llama a "virtual subclass" of Animal
Animal.register(Llama)

llama = Llama()
walk_animal(animal=llama) # <- OK
```

# Protocols
Protocols - structural subtyping (static duck typing) - introduced in python 3.8. `Protocol` is special type of ABC

```python
from typing import Protocol

class EatsBread(Protocol):
    def eat_bread(self):
        pass

def feed_bread(animal: EatsBread):
    animal.eat_bread()

# Duck is implicitely considered to be a subtype of EatsBread
class Duck:
    def eat_bread(self):
        ...

feed_bread(animal=Duck()) # <- OK
```

wrapping up:
- no need to inherit or register
- no more difficalties combining libraries
- need to decaorate your protocol to make `runtime` checkable


