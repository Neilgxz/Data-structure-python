#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

Layer_nums = List[int]


def yh_triangle(nums: List[Layer_nums]) -> int:
    """
    从根节点开始向下走，过程中经过的节点，只需存储经过它时最小的路径和
    :param nums:
    :return:
    """
    assert len(nums) > 0
    n = len(nums)   # 层数
    memo = [[0]*n for i in range(n)]
    memo[0][0] = nums[0][0]

    for i in range(1, n):
        for j in range(i+1):
            # 每一层首尾两个数字，只有一条路径可以到达
            if j == 0:
                memo[i][j] = memo[i-1][j] + nums[i][j]
            elif j == i:
                memo[i][j] = memo[i-1][j-1] + nums[i][j]
            else:
                # 到中间位置的最小路径，可能是从左上或者右上来，选其中最小的。
                memo[i][j] = min(memo[i-1][j-1] + nums[i][j], memo[i-1][j] + nums[i][j])
    return min(memo[n-1])


def yh_triangle_space_optimization(nums: List[Layer_nums]) -> int:
    # 使用一维数组
    assert len(nums) > 0
    n = len(nums)
    memo = [0] * n
    memo[0] = nums[0][0]

    for i in range(1, n):
        for j in range(i, -1, -1):
            if j == i:
                memo[j] = memo[j-1] + nums[i][j]
            elif j == 0:
                memo[j] = memo[j] + nums[i][j]
            else:
                # 注意j是倒着数的，避免了错误覆盖的问题，后一个memo[j]不会调用memo[j+1]
                memo[j] = min(memo[j-1] + nums[i][j], memo[j] + nums[i][j])
    return min(memo)


def yh_triangle_bottom_up(nums: List[Layer_nums]) -> int:
    assert len(nums) > 0
    n = len(nums)
    memo = nums[-1].copy()

    for i in range(n-1, 0, -1):
        for j in range(i):
            memo[j] = min(memo[j] + nums[i-1][j], memo[j+1] + nums[i-1][j])
    return memo[0]


if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle(nums))
    print(yh_triangle_space_optimization(nums))
    print(yh_triangle_bottom_up(nums))
