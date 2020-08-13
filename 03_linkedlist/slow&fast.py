"""
快慢指针的三个应用。1. 链表中环的检测。2.单链表的中间结点。3. 删除倒数第n个结点
"""
from typing import Optional

class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

"""
检测环
快慢双指针，如果相遇一定有环。
在环中，设环的起点到相遇点距离m，slow一共走了k步，fast走2k步，则从头结点到环的起点距离k-m，从相遇点继续走到环起点也为k-m
所以，在相遇后，只要把快慢指针中任意一个重新指向head，然后两指针同速前进k-m步，则会相遇在环的起点
"""
def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            return True
    return False

"""
中间结点
如果链长为奇数，则slow最后为中间结点。因为，fast每次加2，停在n+1位置共n+1步。所以slow走(n+1)/2步正好为中间
如果链长为偶数，则slow和slow+1为中间结点。因为，fast每次加2，停在n位置共n步。所以slow走n/2步正好为中间结点之一，他和slow+1两个为中间结点。
"""
def find_middle_Node(head: Node) -> Optional[Node]:
    slow, fast = head, head
    fast = fast._next if fast else None
    while fast and fast._next:
        slow, fast = slow._next, fast._next._next
    return slow

"""
删除倒数第n个节点。假设n大于0
"""
def remove_nth_from_end(head: Node, n: int) -> Optional[Node]:
    fast = head
    count = 0
    # fast先走n步
    while fast and count < n:
        fast = fast.next
        count += 1
    # 没有足够多的结点，则不删除，输出原链表
    if not fast and count < n:
        return head
    # 刚好n+1个结点，则删除头结点，从第二个结点开始输出
    if not fast and count == n:
        return head.next

    slow = head
    while fast.next:
        fast, slow = fast.next, slow.next
    # 循环结束 fast指向尾结点，slow指向倒数第n+1个结点（尾结点为倒数第1个结点）
    slow.next = slow.next.next
    return head
"""
剑指22. 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        l1 = res
        l2 = res
        for i in range(k):
            l1 = l1.next
        while l1.next:
            l1 = l1.next
            l2 = l2.next
        return l2.next