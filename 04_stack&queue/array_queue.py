"""
    Author: Wenru
"""

from typing import Optional

class DynamicArrayQueue:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0
    
    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            # 当队头未动，队尾指针走到下标为capacity的位置，所有空间都有数据，则不能添加
            if self._head == 0: return False
            # 对头因为出队而向前移动，此时如果还要添加元素，则需要将后面的数据整体向前复制搬移（多余数据不管）
            self._items[0 : self._tail - self._head] = self._items[self._head : self._tail]
            self._tail -= self._head
            self._head = 0
        # 如果队尾指针没有走到capacity
        # 如果队尾指针和队列长度相同，说明没发生过搬移，而且队头指针还在0.此时直接append
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            # 队尾指针与队列长度不同，说明队头发生变动，或者发生过搬移，此时采用覆盖赋值
            self._items[self._tail] = item
        # 队尾指针指向数据的后一位。
        self._tail += 1
        return True
    # 普通队列如果队头和队尾指针未重合，则非空。队头出队
    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
    
    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head:self._tail])

if __name__ == "__main__":
    q = DynamicArrayQueue(10)
    for i in range(10):
        q.enqueue(str(i))
    print(q) # 0 1 2 3 4 5 6 7 8 9

    for _ in range(3):
        q.dequeue()
    print(q) # 3 4 5 6 7 8 9 (7 8 9)
    # 队尾指针与队列长度不同，说明队头发生变动，或者发生过搬移，此时采用覆盖赋值
    q.enqueue("7")  # 3 4 5 6 7 8 9 7 (8 9)
    q.enqueue("8")  # 3 4 5 6 7 8 9 7 8 (9)
    print(q)