#!/usr/bin/python
# -*- coding: UTF-8 -*-
from trie_ import Node, Trie
from queue import Queue


class ACNode(Node):
    def __init__(self, c: str):
        super(ACNode, self).__init__(c)
        self.fail = None
        self.length = 0

    def insert_child(self, c: str):
        self._insert_child(ACNode(c))


class ACTrie(Trie):
    def __init__(self):
        self.root = ACNode(None)


def ac_automata(main: str, ac_trie: ACTrie) -> list:
    root = ac_trie.root
    build_failure_pointer(ac_trie)

    ret = []
    p = root
    for i, c in enumerate(main):
        while p != root and not p.has_child(c):
            p = p.fail

        if p.has_child(c):  # a char matched, try to find all potential pattern matched
            q = p.get_child(c)

            while q != root:

                if q.is_ending_char: #判断失败指针有没有指向一个模式串的结尾
                    ret.append((i-q.length+1, i))

                q = q.fail
            p = p.get_child(c)
        # 树中没有c这个字符，则主串后移一位，看下一个字符
        # 以主串fuck为例, p = root
        # p存在子节点值为f，q = f，不是root也不是模式串结尾，q = q.fail；因为q.fail = root；所以没有找到一个模式串为f，    p = f，p.length = 1，i = 0
        # p存在子节点值为u，q = u，不是root也不是模式串结尾，q = q.fail；因为q.fail = root；所以没有找到一个模式串为u，    p = u，p.length = 2，i = 1
        # p存在子节点值为c，q = c，不是root也不是模式串结尾，q = q.fail；因为q.fail = root；所以没有找到一个模式串为c,uc， p = c，p.length = 3，i = 2
        # p存在子节点值为k，q = k，不是root，  是模式串结尾，q.length = 4，i = 3，ret.append((0,3)) 把要替换成*的敏感字符的start和end坐标保存在ret数组中。
        # 执行q = q.fail，因为q.fail = root；所以没有找到一个模式串为uck,ck,k，p = k
        # 不存在子节点且q不是root，执行p = p.fail = root
        # 一直到s，之前所有字符都不在root的子节点中，无法开启
    return ret


def build_failure_pointer(ac_trie: ACTrie) -> None:
    root = ac_trie.root

    # queue: [(node, node.length) ....]
    # 层次遍历的队列思想，一定会先处理前一层的节点再处理后一层的节点
    node_queue = Queue()
    node_queue.put((root, root.length))

    root.fail = None
    while not node_queue.empty():
        p, length = node_queue.get() # length是目前连续的字符串的长度，也可以理解为抵达的层数 root为0层
        # 在已知p的情况下求p的子节点pc的fail指针。
        for pc in p.children:
            pc.length = length + 1 # 层数加1
            if p == root: 
                pc.fail = root # 第一层节点，都指向root
            else:
                q = p.fail
                # same as kmp
                while q != root and not q.has_child(pc.data):
                    q = q.fail # p的失败指针所指的前缀（或整个模式串）没有下一个子节点等于pc，则要继续向下寻找更短的前缀（或整个模式串）

                # cases now:
                # 1. q == root
                # 2. q != root and q.has_child(pc.data)
                if q.has_child(pc.data):
                    pc.fail = q.get_child(pc.data)
                else:
                    pc.fail = root
            # 按层次遍历，先把p的所有子节点pc的失败指针制定好，再进行
            node_queue.put((pc, pc.length))


if __name__ == '__main__':
    ac_trie = ACTrie()
    ac_trie.gen_tree(['fuck', 'shit', 'TMD', '傻叉'])

    print('--- ac automata ---')
    m_str = 'fuck you, what is that shit, TMD你就是个傻叉傻叉傻叉叉'
    print('original str  : {}'.format(m_str))

    filter_range_list = ac_automata(m_str, ac_trie)
    str_filtered = m_str
    for start, end in filter_range_list:
        str_filtered = str_filtered.replace(str_filtered[start:end+1], '*'*(end+1-start))

    print('after filtered: {}'.format(str_filtered))
