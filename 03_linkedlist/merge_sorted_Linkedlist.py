from typing import Optional
class Node:
    
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

# Merge two sorted linked list
# 有序链表合并
def merge_sorted_list(l1: Node, l2: Node) -> Optional[Node]:
    if l1 and l2:
        p1, p2 = l1, l2
        fake_head = Node(None) # 哨兵
        current = fake_head
        while p1 and p2:
            if p1.data <= p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        current.next = p1 if p1 else p2
        return fake_head.next
    return l1 or l2
