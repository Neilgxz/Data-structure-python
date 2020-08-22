"""
    Author: Wenru Dong
    笔记：
    一个模型：多阶段决策最优解模型
    三个特征：
        最优子结构：最优子结构指的是，问题的最优解包含子问题的最优解。
                   反过来说就是，我们可以通过子问题的最优解，推导出问题的最优解。
                   我们也可以理解为，后面阶段的状态可以通过前面阶段的状态推导出来。
        无后效性：  在推导后面阶段的状态的时候，我们只关心前面阶段的状态值，不关心这个状态是怎么一步一步推导出来的。
                   某阶段状态一旦确定，就不受之后阶段的决策影响。
        重复子问题：不同的决策序列，到达某个相同的阶段时，可能会产生重复的状态。
    两种动态规划解题思路：
        状态转移表法， 状态转移方程法
    四种算法思想比较分析：
        如果我们将这四种算法思想分一下类，那贪心、回溯、动态规划可以归为一类，而分治单独可以作为一类，
        前三个算法解决问题的模型，都可以抽象成我们今天讲的那个多阶段决策最优解模型，
        而分治算法解决的问题尽管大部分也是最优解问题，但是，大部分都不能抽象成多阶段决策模型。

        回溯算法是个“万金油”。基本上能用的动态规划、贪心解决的问题，我们都可以用回溯算法解决。
        回溯算法相当于穷举搜索。穷举所有的情况，然后对比得到最优解。
        不过，回溯算法的时间复杂度非常高，是指数级别的，只能用来解决小规模数据的问题。
        对于大规模数据的问题，用回溯算法解决的执行效率就很低了。

        尽管动态规划比回溯算法高效，但是，并不是所有问题，都可以用动态规划来解决。
        能用动态规划解决的问题，需要满足三个特征，最优子结构、无后效性和重复子问题。
        在重复子问题这一点上，动态规划和分治算法的区分非常明显。
        分治算法要求分割成的子问题，不能有重复子问题，而动态规划正好相反，动态规划之所以高效，就是因为回溯算法实现中存在大量的重复子问题。

        贪心算法实际上是动态规划算法的一种特殊情况。它解决问题起来更加高效，代码实现也更加简洁。不过，它可以解决的问题也更加有限。
        它能解决的问题需要满足三个条件，最优子结构、无后效性和贪心选择性（这里我们不怎么强调重复子问题）。

        其中，最优子结构、无后效性跟动态规划中的无异。“贪心选择性”的意思是，通过局部最优的选择，能产生全局的最优选择。
        每一个阶段，我们都选择当前看起来最优的决策，所有阶段的决策完成之后，最终由这些局部最优解构成全局最优解。
"""

from typing import List
from itertools import accumulate

def min_dist(weights: List[List[int]]) -> int:
    """Find the minimum weight path from the weights matrix.
        从左上到右下，只能向下或向右，求矩阵元素和最小。最小权路径
    """
    m, n = len(weights), len(weights[0]) # m行n列
    table = [[0] * n for _ in range(m)]

    table[0] = list(accumulate(reversed(weights[-1])))
    for i, v in enumerate(accumulate(row[-1] for row in reversed(weights))):
        table[i][0] = v
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = weights[~i][~j] + min(table[i - 1][j], table[i][j - 1])
    return table[-1][-1]


def min_dist_recur(weights: List[List[int]]) -> int:
    #递归法加备忘录
    m, n = len(weights), len(weights[0])
    table = [[0] * n for _ in range(m)]
    def min_dist_to(i: int, j: int) -> int:
        if i == j == 0: return weights[0][0]
        if table[i][j]: return table[i][j]
        min_left = float("inf") if j - 1 < 0 else min_dist_to(i, j - 1)
        min_up = float("inf") if i - 1 < 0 else min_dist_to(i - 1, j)
        return weights[i][j] + min(min_left, min_up)
    return min_dist_to(m - 1, n - 1)


if __name__ == "__main__":
    weights = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    print(min_dist(weights))
    print(min_dist_recur(weights))
