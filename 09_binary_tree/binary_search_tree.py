"""
    Binary search tree

    Author: Wenru Dong
"""
from typing import Optional
import queue
import math
class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self._root = None
      
    def search(self, value: int) -> Optional[TreeNode]:
    # 所有搜索到的节点
        ret = []
        node = self._root
        while node:
            if value < node.val:
                node = node.left
            else:
                if value == node.val:
                    ret.append(node)
                node = node.right
        return ret


    def insert(self, value: int):
        if not self._root:
            self._root = TreeNode(value)
            return
        parent = None
        node = self._root
        while node:
            parent = node
            node = node.left if node.val > value else node.right
        new_node = TreeNode(value)
        if parent.val > value:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, value):

        node = self._root
        parent = None
        while node and node.val != value:
            parent = node
            node = node.left if node.val > value else node.right
        if not node: return
        if parent == None and node != self._root: return
        self._del(node, parent)


    def _del(self, node, parent):

        """
        删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        """

        #1
        if node.left is None and node.right is None:
            # 情况1和2，根节点和普通节点的处理方式不同
            if node == self._root:
                self._root = None
            else:
                if node.val < parent.val:
                    parent.left = None
                else:
                    parent.right = None
        # 2
        elif node.left is None and node.right is not None:
            if node == self._root:
                self._root = node.right
                node.right = None
            elif node.right.val == node.val:
                self._del(node.right,node)
                if node.val < parent.val:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else:
                if node.val < parent.val:
                    parent.left = node.left
                else:
                    parent.right = node.left
                node.right = None

        elif node.left is not None and node.right is None:
            if node == self._root:
                self._root = node.left
                node.left = None
            elif node.left.val == node.val:
                self._del(node.left,node)
                if node.val < parent.val:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                if node.val < parent.val:
                    parent.left = node.left
                else:
                    parent.right = node.left
                node.left = None
        # 3
        else:
            successor = node.right
            successor_parent = node
            while successor.left and successor.val != node.val:
                successor_parent = successor
                successor = successor.left
            if successor.val == node.val:
                self._del(successor,successor_parent)
                self._del(node,parent)
            else:
                node.val = successor.val
                parent, node = successor_parent, successor
                self._del(successor,successor_parent)

    def get_min(self):   
        if self._root is None:
            return None
        n = self._root
        while n.left:
            n = n.left
        return n.val

    def get_max(self):
        if self._root is None:
            return None
        n = self._root
        while n.right:
            n = n.right
        return n.val 

    def __repr__(self):
        # return str(self.in_order())
        print(str(self.in_order()))
        return self._draw_tree()

    def in_order(self):
        """
        中序遍历
        :return:
        """
        if self._root is None:
            return []

        return self._in_order(self._root)

    def _in_order(self, node):
        if node is None:
            return []

        ret = []
        n = node
        ret.extend(self._in_order(n.left))
        ret.append(n.val)
        ret.extend(self._in_order(n.right))     
        return ret

    def _bfs(self):
        """
        bfs
        通过父子关系记录节点编号
        :return:
        """
        if self._root is None:
            return []

        ret = []
        q = queue.Queue()
        # 队列[节点，编号]
        q.put((self._root, 1))

        while not q.empty():
            n = q.get()

            if n[0] is not None:
                ret.append((n[0].val, n[1]))
                q.put((n[0].left, n[1]*2))
                q.put((n[0].right, n[1]*2+1))

        return ret

    def _draw_tree(self):
        """
        可视化
        :return:
        """
        nodes = self._bfs()
        
        if not nodes:
            print('This tree has no nodes.')
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1
        
        prt_nums = []
        
        for i in range(layer_num):
            prt_nums.append([None]*2**i)

        for v, p in nodes:
            row = int(math.log(p ,2))
            col = p % 2**row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'

        return prt_str
# 返回深度
def maxDepth(root):
    if root is None: 
         return 0
    else: 
        left_height = maxDepth(root.left) 
        right_height = maxDepth(root.right) 
        return max(left_height, right_height) + 1


if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    bst.insert(6)
    bst.insert(1)
    bst.insert(7)
    bst.insert(3)

    # 插入
    bst.insert(1)
    bst.insert(4)
    print(bst)

    # 搜索
    for n in bst.search(1):
        print(n.val)

    # 删除
    bst.insert(6)
    bst.insert(7)
    print(bst)
    bst.delete(7)
    print(bst)
    bst.delete(6)
    print(bst)
    bst.delete(4)
    print(bst)

    # min max
    print(bst.get_max())
    print(bst.get_min())

    depth = maxDepth(bst._root)
    print(depth)
