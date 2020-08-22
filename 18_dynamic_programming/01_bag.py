#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Tuple


def bag(items_info: List[int], capacity: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大重量

    :param items_info: 每个物品的重量
    :param capacity: 背包容量
    :return: 最大装载重量
    笔记：
    前一节中运用的回溯算法复杂度比较高，求解过程如果用递归树画出来，其中有一些子问题的求解是重复的。O(2^n)
    我们可以借助“备忘录”的解决方式，记录已经计算过的情况，下次再遇到就不用计算直接return回结果
    这种解决方法非常好。实际上，它已经跟动态规划的执行效率基本上没有差别。但是，多一种方法就多一种解决思路，我们现在来看看动态规划是怎么做的。

    动态规划(Dynamic Programming):
    我们把整个求解过程分为 n 个阶段，每个阶段会决策一个物品是否放到背包中。
    每个物品决策（放入或者不放入背包）完之后，背包中的物品的重量会有多种情况，也就是说，会达到多种不同的状态，对应到递归树中，就是有很多不同的节点。
    我们把每一层重复的状态（节点）合并，只记录不同的状态，然后基于上一层的状态集合，来推导下一层的状态集合。
    我们可以通过合并每一层重复的状态，这样就保证每一层不同状态的个数都不会超过 w+1 个（w 表示背包的承载重量），也就是例子中的 9+1。
    于是，我们就成功避免了每层状态个数的指数级增长。O(n*w)
    
    补充：
    可以将二维数组改为一维数组减少空间的消耗。后一个物品会在前一个物品基础上添加和覆盖状态。
    注意循环时要从后往前判断. 比如说第0个物品重量为3.则memo[0]=memo[3]=true.
    第1个物品假设重量为1，如果从前往后判断 memo[0]= memo[1] = true, 之后本应该去从memo[3]开始考虑 但是循环会在memo[1]的基础上加。
    就导致了memo[2]=1这个本不该出现的情况

    双十一凑满减问题：
    带价格的01背包问题。购物车中有 n 个商品。我们针对每个商品都决策是否购买。每次决策之后，对应不同的状态集合。我们还是用一个二维数组 memo[n][x]，
    来记录每次决策之后所有可达的状态。不过，这里的 x 值是多少呢？0-1 背包问题中，我们找的是小于等于 w 的最大值，x 就是背包的最大承载重量 w+1。
    对于这个问题来说，我们要找的是大于等于 200（满减条件）的值中最小的，所以就不能设置为 200 加 1 了。
    就这个实际的问题而言，如果要购买的物品的总价格超过 200 太多，比如 1000，那这个羊毛“薅”得就没有太大意义了。
    所以，我们可以限定 x 值为 1001。不过，这个问题不仅要求大于等于 200 的总价格中的最小的，我们还要找出这个最小总价格对应都要购买哪些商品。
    实际上，我们可以利用 states 数组，倒推出这个被选择的商品序列。状态 (i, j) 只有可能从 (i-1, j) 或者 (i-1, j-value[i]) 两个状态推导过来。
    所以，我们就检查这两个状态是否是可达的，也就是 states[i-1][j]或者 states[i-1][j-value[i]]是否是 true。
    如果 states[i-1][j]可达，就说明我们没有选择购买第 i 个商品，如果 states[i-1][j-value[i]]可达，那就说明我们选择了购买第 i 个商品。
    我们从中选择一个可达的状态（如果两个都可达，就随意选择一个），然后，继续迭代地考察其他商品是否有选择购买。
    """
    n = len(items_info)
    # 二维数组memo，来记录每层可以达到的不同状态
    memo = [[-1]*(capacity+1) for i in range(n)]
    # 第0个物品重量items_info[0]。要么装入背包，要么不装入背包，决策完之后，会对应背包的两种状态，
    # 背包中物品的总重量是 0 或者 items_info[0]。我们用 memo[0][0]=1 和 memo[0][items_info[0]]=1 来表示这两种状态。
    memo[0][0] = 1
    if items_info[0] <= capacity:
        memo[0][items_info[0]] = 1
    # 之后的每一种状态都基于之前的背包状态。
    for i in range(1, n):
        for cur_weight in range(capacity+1):
            # 在第i-1个物品决策完之后所有可能的重量情况下分别决策第i个物品是否装入背包
            # 更新第i层的可能状态。
            if memo[i-1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i-1][cur_weight]   # 不选
                if cur_weight + items_info[i] <= capacity:    # 选
                    memo[i][cur_weight + items_info[i]] = 1
    # 结束时在最后一个物品决策玩之后的状态中，从后往前选状态中重量最大的。
    for w in range(capacity, -1, -1):
        if memo[-1][w] != -1:
            return w


def bag_with_max_value(items_info: List[Tuple[int, int]], capacity: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大价值

    :param items_info: 物品的重量和价值
    :param capacity: 背包容量
    :return: 最大装载价值
    """
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 0
    if items_info[0][0] <= capacity:
        memo[0][items_info[0][0]] = items_info[0][1]

    for i in range(1, n):
        for cur_weight in range(capacity+1):
            if memo[i-1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i-1][cur_weight] # 不选第i个物品，总价值不变
                if cur_weight + items_info[i][0] <= capacity:
                    memo[i][cur_weight + items_info[i][0]] = max(memo[i][cur_weight + items_info[i][0]], # 旧状态的价值
                                                                 memo[i-1][cur_weight] + items_info[i][1]) # 新状态的价值
    return max(memo[-1])


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(bag(items_info, capacity))

    # [(weight, value), ...]
    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    capacity = 8
    print(bag_with_max_value(items_info, capacity))
