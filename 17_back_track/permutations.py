#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

permutations_list = []  # 全局变量，用于记录每个输出


def permutations(nums: List, n: int, pick_count: int):
    """
    从nums选取n个数的全排列

    回溯法，用一个栈记录当前路径信息
    当满足n==0时，说明栈中的数已足够，输出并终止遍历
    :param nums:
    :param n:
    :param pick_count:
    :return:
    """
    if n == 0:
        print(permutations_list)
    else:
        for i in range(len(nums) - pick_count):
            # 每次先固定第i个放进排列列表
            permutations_list[pick_count] = nums[i]
            # 把固定好的第i个放到数组nums的后面和permutations_list[pick_count]，不让他参与接下来的排列。
            nums[i], nums[len(nums) - pick_count - 1] = nums[len(nums) - pick_count - 1], nums[i]
            # pick_count+1说明已经选出一个固定的数字并且已经放到尾部len(nums) - pick_count - 1下标的位置
            # 问题变成除了固定数以外的数组，选取n-1个数的全排列问题。
            permutations(nums, n-1, pick_count+1)
            # 完成一次排列，把数组恢复原样，用来进行下一次循环。
            nums[i], nums[len(nums) - pick_count - 1] = nums[len(nums) - pick_count - 1], nums[i]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    n = 3
    print('--- list ---')
    print(nums)

    print('\n--- pick num ---')
    print(n)

    print('\n--- permutation list ---')
    permutations_list = [0] * n
    permutations(nums, n, 0)

