from single_Linkedlist import SingleLinkedList
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkedList(SingleLinkedList):
    """双向链表"""
# init，判空，长度，遍历，search 不需要重写。
    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将head指向node
            self.head = node
        else:
            # 将node的next指向head的头节点
            node.next = self.head
            # 将head的头节点的prev指向node
            self.head.prev = node
            # 将head 指向node
            self.head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将head指向node
            self.head = node
        else:
            # 移动到链表尾部
            cur = self.head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.head
            count = 0
            # 移动到指定位置
            while count < pos :
                count += 1
                cur = cur.next
            # 将node的next指向cur
            node.next = cur
            # 将node的prev指向cur的前一个节点
            node.prev = cur.prev
            # 将cur的前一个节点的next指向node
            cur.prev.next = node
            # 将cur的prev指向node
            cur.prev = node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self.head
            while cur != None:
                if cur.item == item:
                    # 如果首节点的元素即是要删除的元素
                    if cur == self.head:
                        self.head = cur.next
                        if cur.next:
                            # 不只有一个结点时执行
                            cur.next.prev = None
                    else:
                        # 将cur的前一个节点的next指向cur的后一个节点
                        cur.prev.next = cur.next
                        if cur.next:
                            # 不是尾结点时执行
                            # 将cur的后一个节点的prev指向cur的前一个节点
                            cur.next.prev = cur.prev
                    break
                else:
                    cur = cur.next
if  __name__ == "__main__":
    ll = DoubleLinkedList()
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