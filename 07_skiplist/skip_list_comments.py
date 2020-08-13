"""
    An implementation of skip list.
    The list stores positive integers without duplicates.
    跳表的一种实现方法。
    跳表中储存的是正整数，并且储存的是不重复的。
    Author: Ben
    笔记：对链表改造，支持类似二分的查找算法，跳表(Skiplist)
    1.  跳表是一种动态数据结构。通过在原链表之上简历索引层，使查找一个结点需要遍历的结点数减少，提高查找效率。
    2.  时间复杂度：
        若每两个结点会抽出一个结点作为上一级索引的结点，那第一级索引的结点个数大约就是 n/2，第二级索引的结点个数大约就是 n/4，第三级索引的结点个数大约就是 n/8，依次类推，
        也就是说，第 k 级索引的结点个数是第 k-1 级索引的结点个数的 1/2，那第 k级索引结点的个数就是 n/(2k)。
        假设索引有 h 级，最高级的索引有 2 个结点。通过上面的公式，我们可以得到 n/(2h)=2，
        从而求得 h=log2n-1。如果包含原始链表这一层，整个跳表的高度就是 log2n。我们在跳表中查询某个数据的时候，
        如果每一层都要遍历 m 个结点，那在跳表中查询一个数据的时间复杂度就是 O(m*logn)。
        假设我们要查找的数据是 x，在第 k 级索引中，我们遍历到 y 结点之后，发现 x 大于 y，小于后面的结点 z，所以我们通过 y 的 down 指针，从第 k 级索引下降到第 k-1 级索引。
        在第 k-1 级索引中，y 和 z 之间只有 3 个结点（包含 y 和 z），所以，我们在 K-1 级索引中最多只需要遍历 3 个结点，依次类推，每一级索引都最多只需要遍历 3 个结点
        通过上面的分析，我们得到 m=3，所以在跳表中查询任意数据的时间复杂度就是 O(logn)。
        这种查询效率的提升，前提是建立了很多级索引，也就是空间换时间的设计思路。
    3.  空间复杂度：
        假设原始链表大小为 n，那第一级索引大约有 n/2 个结点，第二级索引大约有 n/4 个结点，
        以此类推，每上升一级就减少一半，直到剩下 2 个结点。如果我们把每层索引的结点数写出来，就是一个等比数列。
        这几级索引的结点总和就是 n/2+n/4+n/8…+8+4+2=n-2。所以，跳表的空间复杂度是 O(n)。
        也就是说，如果将包含 n 个结点的单链表构造成跳表，我们需要额外再用接近 n 个结点的存储空间。
        通过改变每层索引的结点数可以减少需要的存储空间，但是软件开发中，一般不在意索引占用的二外空间，因为原始链表存储的可能是很大的对象
        而索引结点只存储关键值和几个指针不用存储对象。所以当对象比索引结点大很多时，那索引占用的额外空间就可以忽略了。
    3.  高效的动态插入和删除 O(logn)
    4.  跳表索引动态更新：
        如果不更新索引，就会出现某两个索引结点之间数据非常多的情况。
        可以通过随机函数来决定将结点插入到哪几级索引中。第一到第K级
    5.  Radis为什么用跳表来实现有序集合，而不是红黑树？
        Radis中有序集合支持的操作有：插入，删除，查找，按区间查找，迭代输出有序序列。
        跳表优点：
            1.  按照区间查找，跳表比红黑树效率高。跳表只需要O(logn)的时间复杂度定位区间的起点，然后在原始链表中顺序往后遍历就可以了。这样做非常高效。
            2.  跳表的代码更容易实现。
        跳表缺点：
            跳表没有现成的实现，红黑树可以直接拿来用。
"""
import random
class SkipListNode:
    def __init__(self, val, high=1):
        # 节点存储的值
        self.data = val
        # 节点对应索引层的深度。.deeps相当于.next.注明相同层数
        self.deeps = [None] * high

class SkipList(object):
    def __init__(self):
        # 索引层的最大深度
        self.__MAX_LEVEL = 16
        # 跳表的高度
        self._high = 1
        # 每一索引层的首节点, 默认值为None
        self._head = SkipListNode(None, self.__MAX_LEVEL)

    def find(self, val):
        cur = self._head
        # 从索引的顶层, 逐层定位要查找的值
        # 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
        for i in range(self._high - 1, -1, -1):
            # 同一索引层内, 查找小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]

        if cur.deeps[0] and cur.deeps[0].data == val:
            return cur.deeps[0]
        return None

    def insert(self, val):
        '''
        新增时, 通过随机函数获取要更新的索引层数,
        要对低于给定高度的索引层添加新结点的指针
        '''
        high = self.randomLevel()
        if self._high < high:
            self._high = high
        # 申请新结点
        newNode = SkipListNode(val, high)
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [self._head] * high
        cur = self._head

        # 在低于随机高度的每一个索引层寻找小于插入值的节点
        for i in range(high - 1, -1, -1):
            # 每个索引层内寻找小于带插入值的节点
            # ! 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur

        # 在小于高度的每个索引层中插入新结点
        for i in range(high):
            # new.next = prev.next \ prev.next = new.next
            newNode.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = newNode
        """
        一开始初始化self.head为None，self.head.deeps指向16个None分别对应每一层。
        insert函数，假设第一次随机插入4层。newNode初始值为1，newNode.deeps指向4个None, newNode.deeps[0]...
        cur = self.head循环因为cur.deeps都是None所以不进行 
        cache[i] = cur意思是例如cache[0]也等于self.head，就也有16个cache[0].deeps，cache[0].deeps[0]...
        新的循环插入newNode。例如newNode.deeps[0] = cache[0].deeps[0]讲newNode在第0层的deeps指向cache[0].deeps[0]，也就是None.
        类似于平时我们写的 newNode.next = self.head.next
        cache[i].deeps[i] = newNode  也相当于 我们平时写的 self.head.next = newNode
        相当于self.head一直指向哨兵结点None 输出的时候从self.head.next开始输出。
        """
    def delete(self, val):
        '''
        删除时, 要将每个索引层中对应的节点都删掉
        '''
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * self._high
        cur = self._head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(self._high - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur
        # 如果给定的值存在, 更新索引层中对应的节点
        if cur.deeps[0] and cur.deeps[0].data == val:
            for i in range(self._high):
                if cache[i].deeps[i] and cache[i].deeps[i].data == val:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]

    def randomLevel(self, p=0.25):
        '''
        #define ZSKIPLIST_P 0.25      /* Skiplist P = 1/4 */
        https://github.com/antirez/redis/blob/unstable/src/t_zset.c
        '''
        high = 1
        for _ in range(self.__MAX_LEVEL - 1):
            if random.random() < p:
                high += 1
        return high

    def __repr__(self):
        vals = []
        p = self._head
        while p.deeps[0]:
            vals.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return '->'.join(vals)


if __name__ == '__main__':
    sl = SkipList()
    for i in range(10):
        sl.insert(i)
    print(sl)
    p = sl.find(7)
    print(p.data)
    sl.delete(4)
    print(sl)
    sl.delete(4.5)
    print(sl)
