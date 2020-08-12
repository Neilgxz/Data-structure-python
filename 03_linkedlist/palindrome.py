"""
    check a single-linked list whether a palindrome
"""
class Node:

    def __init__(self, data: int, next_node=None):
        self.data = data
        self.next = next_node
        
class SinglyLinkedList:

    def __init__(self):
        self._head = None
    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node:
            new_node.next = self._head
            self._head = new_node

    def __repr__(self) -> str:
        nums = []
        current = self._head
        while current:
            nums.append(current.data)
            current = current.next
        return "->".join(str(num) for num in nums)

    # 重写__iter__方法，方便for关键字调用打印值
    def __iter__(self):
        node = self._head
        while node:
            yield node.data
            node = node.next

    def print_all(self):
        current = self._head
        if current:
            print(f"{current.data}", end="")
            current = current.next
        while current:
            print(f"->{current.data}", end="")
            current = current.next
        print("")

def reverse(head):
    reverse_head = None
    while head:
        next = head.next
        head.next = reverse_head
        reverse_head = head
        head = next
    return reverse_head

def is_palindrome(l):
    l.print_all()
    slow = l._head
    fast = l._head
    position = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        position += 1

    reverse_node = reverse(slow)
    head_node = l._head
    is_palin = True
    while (head_node and reverse_node):
        if (head_node.data == reverse_node.data):
            head_node = head_node.next
            reverse_node = reverse_node.next
        else:
            is_palin = False
            break
    return is_palin

if __name__ == '__main__':
    # the result should be False, True, True, True, True
    test_str_arr = ['ab', 'aa', 'aba', 'abba', 'abcba']
    for str in test_str_arr:
        l = SinglyLinkedList()
        for i in str:
            l.insert_value_to_head(i)

        print(is_palindrome(l))



