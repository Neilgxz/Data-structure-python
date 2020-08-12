class Node:
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedlist:
    """单向循环链表"""
    def __init__(self, node=None):
        self.head = None
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        # 尾结点不操作 count = 1起步
        count = 1
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.head
        while cur.next != self.head:
            print(cur.item, end=" ")
            cur = cur.next
        # 尾结点再打印一次
        print(cur.item)

    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            #退出循环, cur指向尾结点
            node.next = self.head
            self.head = node
            cur.next = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            # 移到链表尾部
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点head
            node.next = self.head

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            pre = self.head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.head
        while cur.next != self.head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        # 尾结点再判断一次
        if cur.item == item:
            return True
        return False

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self.head
        pre = None
        while cur.next != self.head:
            if cur.item == item:
                if cur == self.head:
                    # 删除头结点
                    rear = self.head
                    while rear.next != self.head:
                        rear = rear.next
                    self.head = cur.next
                    rear.next = self.head
                else:
                    # 删除中间结点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 循环结束
        if cur.item == item:
            if cur == self.head:
                # 只有一个节点
                self.head = None
            else:
                # 删除尾结点
                pre.next = cur.next

if __name__ == "__main__":
    ll = SinCycLinkedlist()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()