"""
**Бинарное дерево - это граф, где у каждой вершины не более 2 детей (вершин)

Куча (бинарная куча) посроена на бинарном дереве, где соблюдены свойтсва
    1. Дерево бинарное
    2. Дерево полное
    3. Дерево не направленное
    4. Каждая вершина (ребенок) меньше либо равно значению родителя

Преимущество бинарной кучи в том, что для хранения структуры мы используем массив.
Находить родителя, левого и правого сыновей можно по формулам:
    parent(i)     = (i - 1) / 2
    leftChild(i)  = 2 * i + 1
    rightChild(i) = 2 * i + 2

    
https://www.youtube.com/watch?v=itnTrxrmtZ0
"""

from typing import List, Optional


class BinaryHeap:
    def __init__(
        self, elements: Optional[List[int]] = None
    ) -> None:
        self._length = None

        if elements is None:
            self.elements: List[int] = []
        else:
            self.heap(elements)
    
    @property
    def length(self) -> int:
        self._length = len(self.elements)
        return self._length

    def add(self, element: int) -> None:
        self.elements.append(element)

        current_idx = self.length - 1
        parent = int((current_idx - 1) / 2)

        # until reach root and pivot element grater than parent 
        while current_idx < 0 and list[current_idx] > list[parent]:
            list[current_idx], list[parent] = list[parent], list[current_idx]
            current_idx = parent
            parent = int((current_idx - 1) / 2)
    
    def heapify(self, idx: int) -> None:
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self._length:
            if (self.elements[idx] < self.elements[left]):
                self.elements[idx], self.elements[left] = self.elements[left], self.elements[idx]
                self.heapify(left)
        if right < self._length:
            if (self.elements[idx] < self.elements[right]):
                self.elements[idx], self.elements[right] = self.elements[right], self.elements[idx]
                self.heapify(right)
        

    def heap(self, elements: List[int]) -> None:
        self.elements = elements
        start, stop, step = int(self.length / 2 + 1), -1, -1
        for idx in range(start, stop, step):
            self.heapify(idx)


bh = BinaryHeap(elements=[10, 1, 99, 250, 50, 1000, 10000, 12])