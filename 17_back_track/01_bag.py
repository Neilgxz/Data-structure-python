#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
01背包：我们有一个背包，背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，价值也不同，并且不可分割。我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总价值最大？
"""
from typing import List

# 背包选取的物品列表
picks = []
picks_with_max_value = []


def bag(capacity: int, cur_weight: int, items_info: List, pick_idx: int):
    """
    回溯法解01背包，穷举
    :param capacity: 背包容量
    :param cur_weight: 背包当前重量
    :param items_info: 物品的重量和价值信息
    :param pick_idx: 当前物品的索引
    :return:
    """
    # 考察完所有物品，或者在中途已经装满
    if pick_idx >= len(items_info) or cur_weight == capacity:
        global picks_with_max_value
        if get_value(items_info, picks) > \
                get_value(items_info, picks_with_max_value):
            picks_with_max_value = picks.copy()
    else:
        item_weight = items_info[pick_idx][0]
        if cur_weight + item_weight <= capacity:    # 选
            picks[pick_idx] = 1
            bag(capacity, cur_weight + item_weight, items_info, pick_idx + 1)

        picks[pick_idx] = 0                         # 不选
        bag(capacity, cur_weight, items_info, pick_idx + 1)
    # 重量优先能选就选，当有一个不能选为0，回溯时会先把它前一个选了的改为不选 1 改为 0。之后在继续能选就选
    # picks : 1 1 1 1 0 picks_with_max_value 1 1 1 1 0
    # picks : 1 1 1 0 0
    # picks : 1 1 0 1 0
    # picks : 1 1 0 0 0
    # picks : 1 0 1 1 0
    # picks : 1 0 1 0 1 picks_with_max_value 1 0 1 0 1
    # picks : 1 0 0 1 1
    # picks : 1 0 0 1 0
    # picks : 1 0 0 0 1
    # picks : 1 0 0 0 0
    # picks : 1 0 0 0 0
    # picks : 0 1 1 1 1
    # ...

def get_value(items_info: List, pick_items: List):
    values = [_[1] for _ in items_info]
    return sum([a*b for a, b in zip(values, pick_items)])


if __name__ == '__main__':
    # [(weight, value), ...]
    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    capacity = 8

    print('--- items info ---')
    print(items_info)

    print('\n--- capacity ---')
    print(capacity)

    picks = [0] * len(items_info)
    bag(capacity, 0, items_info, 0)

    print('\n--- picks ---')
    print(picks_with_max_value)

    print('\n--- value ---')
    print(get_value(items_info, picks_with_max_value))
