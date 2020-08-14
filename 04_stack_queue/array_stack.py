"""
    Stack based upon array
    用数组实现的栈

    Author: Guixiang
"""

from typing import Optional


class ArrayStack:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._top = 0

    def push(self, item: str) -> bool:
        if self._top == self._capacity:
            return False
        self._items.append(item)
        self._top += 1
        return True

    def pop(self) -> Optional[str]:
        if self._items:
            item = self._items[self._top-1]
            self._items[self._top-1] = None
            self._top -= 1
            return item
        else:
            return None

if __name__ == "__main__":
    a = ArrayStack(3)
    print(a.pop())
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())