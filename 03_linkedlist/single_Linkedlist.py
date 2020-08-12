"""
单链表
笔记：边界条件处理 ：空链表，只有一个结点，只有两个结点，处理头节点和尾结点。
"""
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkedList:

    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self.head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")
    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = Node(item)
        # 将新节点的链接域next指向头节点，即head指向的位置
        node.next = self.head
        # 将链表的头_head指向新节点
        self.head = node
    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        # 先判断链表是否为空，若是空链表，则将head指向新节点
        if self.is_empty():
            self.head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = Node(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
    def remove(self,item):
        """删除节点"""
        cur = self.head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if cur == self.head:
                    # 将头指针指向头节点的后一个节点
                    self.head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

# 链表无法像顺序表一样随机读取，增加指针域空间开销大，但存储空间使用要相对灵活
# 链表 访问元素O(1) 头插删O(1) 尾插删O(n) 中插删O(n)
# 顺序表 访问元素O(1) 头插删O(n) 尾插删O(1) 中插删O(n)
if __name__ == "__main__":
    ll=SingleLinkedList()
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
    ll.insert(-1,9)
    ll.travel()
    ll.insert(3,100)
    ll.travel()
    ll.insert(10,200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()