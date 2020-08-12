class Stack:
    """栈"""
    def __init__(self):
         self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self, item):
        """加入元素"""
        self.items.append(item)

    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        #return self.items[len(self.items)-1]
        if self.is_empty():
            return None
        else:
            return self.items[-1]
    def size(self):
        """返回栈的大小"""
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())