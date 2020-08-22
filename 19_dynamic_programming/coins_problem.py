#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
硬币找零问题
"""
from typing import List


def coins_dp(values: List[int], target: int) -> int:
    # memo[i]表示target为i的时候，所需的最少硬币数
    memo = [0] * (target+1)
    # 0元的时候为0个
    memo[0] = 0

    for i in range(1, target+1):
        min_num = 999999
        # 对于values中的所有n
        # memo[i]为 min(memo[i-n1], memo[i-n2], ...) + 1
        for n in values:
            if i >= n:
                min_num = min(min_num, 1 + memo[i-n])
            else:   # values中的数值要从小到大排序
                break
        memo[i] = min_num
    # i = 1; n = 1; min_num = 1; memo[1] = 1
    # i = 2; n = 1; min_num = 2; memo[2] = 1
    # i = 3; n = 1; min_num = 3;
    # i = 3; n = 3; min_num = 1 + memo[3-3] = 1; memo[3] = 1 

    # print(memo)
    return memo[-1]


min_num = 999999
def coins_backtracking(values: List[int], target: int, cur_value: int, coins_count: int):
    if cur_value == target:
        global min_num
        min_num = min(coins_count, min_num)
    else:
        for n in values:
            if cur_value + n <= target:
                coins_backtracking(values, target, cur_value+n, coins_count+1)


if __name__ == '__main__':
    values = [1, 3, 5]
    target = 23
    print(coins_dp(values, target))
    coins_backtracking(values, target, 0, 0)
    print(min_num)

