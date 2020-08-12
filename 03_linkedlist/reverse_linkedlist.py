# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            head.next, last, head = last, head, head.next
        return last

    def reverseList_1(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        p = self.reverseList_1(head.next)
        head.next.next =head
        head.next = None
        return p
if __name__ == "__main__":
    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    reversed = Solution()
    a = reversed.reverseList(head)
    # a = reversed.reverseList_1(head)
    print(a.val)
    print(a.next.val)
    print(a.next.next.val)
    print(a.next.next.next.val)
    print(a.next.next.next.next.val)