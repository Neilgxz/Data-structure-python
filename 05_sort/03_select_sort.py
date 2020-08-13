"""
选择排序：最优O(n) 最坏,平均 O(n^2) 原地排序
不稳定：比如 5，8，5，2，9 这样一组数据，
使用选择排序算法来排序的话，第一次找到最小元素 2，与第一个 5 交换位置，那第一个 5 和中间的 5 顺序就变了，所以就不稳定了。
正是因此，相对于冒泡排序和插入排序，选择排序就稍微逊色了。
"""
from typing import List
def select_sort(alist):
    n = len(alist)
    for j in range(n-1): # 最后一位不用排序
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)