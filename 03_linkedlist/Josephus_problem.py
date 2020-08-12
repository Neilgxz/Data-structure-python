"""
单向循环列表，约瑟夫问题:
人们站在一个等待被处决的圈子里，计数从圆圈中的指定点开始，并沿指定方向围绕圆圈进行。在跳过指定数量的人之后，处刑下一个人。对剩下的人重复该过程，
从下一个人开始，朝同一方向跳过相同数量的人，直到只剩下一个人，并被释放。
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# 构建循环列表，1 2 3 4 ... n
def create_linkedList(n):
    head = Node(1)
    pre = head
    for i in range(2, n+1):
        newNode = Node(i)
        pre.next= newNode
        pre = newNode
    pre.next = head
    return head

n = 5 # 总人数
m = 2 # 每m个人处刑1人
if m == 1: # 如果是1的话，特殊处理，直接输出最后一人存活。
    print (n)
else:
    head = create_linkedList(n)
    pre = None
    cur = head
    while cur.next != cur: # 终止条件是节点的下一个节点指向本身
        for i in range(m-1):
            pre = cur
            cur = cur.next
        print (cur.value)
        pre.next = cur.next
        cur.next = None
        cur = pre.next
    print (cur.value)
