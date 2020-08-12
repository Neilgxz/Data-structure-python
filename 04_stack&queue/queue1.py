class Queue:
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.append(item)

    def dequeue(self):
        """出队列"""
        return self.items.pop(0)

    def size(self):
        """返回大小"""
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print (q.dequeue())
    print (q.dequeue())
    print (q.dequeue())