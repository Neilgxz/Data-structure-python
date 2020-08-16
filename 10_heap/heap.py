#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import random


class Heap:
    def __init__(self, nums=None, capacity=100):
        # 下标从0开始的数组构成堆
        self._data = []
        self._capacity = capacity
        # 初始可以输入为一个列表
        if type(nums) == list and len(nums) <= self._capacity:
            for n in nums:
                assert type(n) is int
                self._data.append(n)
        self._length = len(self._data)
        # 建堆
        self.build_heap()
    # 从上向下堆化所有非叶子节点，用于建堆
    def build_heap(self):
        if self._length <= 1:
            return

        # idx of the Last Parent node
        lp = (self._length - 2) // 2

        for i in range(lp, -1, -1):
            self._heap_down(i)

    def _heap_down(self, idx):
        pass

    def insert(self, num):
        pass
    # 获得堆顶元素
    def get_top(self):
        if self._length <= 0:
            return None
        return self._data[0]
    # 移除堆顶元素，采用从上至下的堆化
    def remove_top(self):
        if self._length <= 0:
            return None
        # 先交换尾元素和堆顶元素
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        # 删除此时的尾元素
        ret = self._data.pop()
        self._length -= 1
        # 堆化堆顶元素
        self._heap_down(0)

        return ret

    def get_data(self):
        return self._data

    def get_length(self):
        return self._length

    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return 'empty heap'

        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            # 每行最后一个换行 int(math.log(i+1, 2)+1) 是当前层数，根为第1层
            # 所以2**int(math.log(i+1, 2)+1) - 1 是当前所有层都装满时的结点数，数量再-1就是列表下标。
            if i == 2 ** int(math.log(i + 1, 2) + 1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret

    def __repr__(self):
        return self._draw_heap(self._data)

# 大顶堆
class MaxHeap(Heap):
    # 大顶堆 从上向下堆化下标为idx的元素
    def _heap_down(self, idx):
        if self._length <= 1:
            return
        # 最后一个非叶子节点的下标
        lp = (self._length - 2) // 2

        while idx <= lp:
            lc = 2 * idx + 1
            rc = lc + 1

            if rc <= self._length-1:
                tmp = lc if self._data[lc] > self._data[rc] else rc
            else:
                tmp = lc

            if self._data[tmp] > self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break
    # 大顶堆 插入，从下向上的堆化
    def insert(self, num):
        if self._length >= self._capacity:
            return False

        self._data.append(num)
        self._length += 1

        nn = self._length - 1
        while nn > 0:
            p = (nn-1) // 2

            if self._data[nn] > self._data[p]:
                self._data[nn], self._data[p] = self._data[p], self._data[nn]
                nn = p
            else:
                break

        return True
    # 大顶堆，堆排序 从小到大
    def sort(self):
        # sort
        for i in range(self._length-1, 0, -1):
            self._data[0], self._data[i] = self._data[i], self._data[0]
            self._length -= 1
            self._heap_down(0)
        self._length = len(self._data)
        return


class MinHeap(Heap):
    # 小顶堆 从上向下堆化下标为idx的元素
    def _heap_down(self, idx):
        if self._length <= 1:
            return

        lp = (self._length - 2) // 2

        while idx <= lp:
            lc = 2 * idx + 1
            rc = lc + 1

            if rc <= self._length-1:
                tmp = lc if self._data[lc] < self._data[rc] else rc
            else:
                tmp = lc

            if self._data[tmp] < self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break
    # 小顶堆 插入，从下向上的堆化
    def insert(self, num):
        if self._length >= self._capacity:
            return False

        self._data.append(num)
        self._length += 1

        nn = self._length - 1
        while nn > 0:
            p = (nn-1) // 2

            if self._data[nn] < self._data[p]:
                self._data[nn], self._data[p] = self._data[p], self._data[nn]
                nn = p
            else:
                break

        return True
    # 小顶堆，堆排序 从大到小
    def sort(self):
        # sort
        for i in range(self._length-1, 0, -1):
            self._data[0], self._data[i] = self._data[i], self._data[0]
            self._length -= 1
            self._heap_down(0)
        self._length = len(self._data)
        return


if __name__ == '__main__':
    nums = list(range(10))
    random.shuffle(nums)

    max_h = MaxHeap(nums)
    print('--- max heap ---')
    print(max_h)

    max_h.sort()
    print('--- after sort ---')
    print(max_h)


    print('--- min heap ---')
    min_h = MinHeap(nums)
    print(min_h)

    min_h.sort()
    print('--- after sort ---')
    print(min_h)