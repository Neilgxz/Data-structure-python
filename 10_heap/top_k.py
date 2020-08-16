#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
from heap import MinHeap


def top_k(nums, k):
    """
    返回数组的前k大元素
    :param nums:
    :param k:
    :return:
    """
    if len(nums) <= k:
        return nums
    # 先把nums列表的前k个元素构成小顶堆，大于等于堆顶元素的有k-1个，整个堆为前k大元素
    min_h = MinHeap(nums[:k], k)
    # 其余各个元素 如果大于堆顶元素，则把堆顶元素移除，并添加新元素并从下到上堆化
    for i in range(k, len(nums)):
        tmp = min_h.get_top()
        if nums[i] > tmp:
            min_h.remove_top()
            min_h.insert(nums[i])

    return min_h.get_data()


if __name__ == '__main__':
    nums = []
    k = 3

    for i in range(20):
        nums.append(random.randint(1, 100))

    print('--- nums ---')
    print(nums)

    print('--- top {} ---'.format(k))
    print(top_k(nums, k))
