class Node:
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self,node):
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item, end=" ")
        self.inorder(node.rchild)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.item, end=" ")

    # 二叉树的最大深度(Depth > 0)
    def maxDepth(self, root: Node) -> int:
        if root is None: 
            return 0 
        else: 
            left_Depth = self.maxDepth(root.lchild) 
            right_Depth = self.maxDepth(root.rchild) 
            return max(left_Depth, right_Depth) + 1

if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
    print(" ")
    Depth = tree.maxDepth(tree.root)
    print(Depth)






