"""
插入排序 最优O(n) 最坏O(n^2)。每次插入操作都相当于在数组中插入一个数据，循环执行 n 次插入操作，所以平均时间复杂度为 O(n2)。
稳定，原地排序
通过构建有序序列，对未排序数据，在已排序序列中从后向前扫描，找到相应位置插入。
扫描过程中，需要反复把已排序的元素逐步向后挪位，为最新元素提供插入空间
"""
from typing import List

def insert_sort(alist: List[int]):
    n = len(alist)
    for j in range(1,n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)