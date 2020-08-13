"""
希尔排序：在插入排序的基础上，先将序列用gap分成几组。在组内进行插入排序后合并，再改变gap值重新分组排序。
直到gap=1相当于普通的插入排序，最优复杂度 根据步长序列不同而不同O(n^1.3)，最坏O(n^2) gap=1 平均O(nlogn)~O(n^2) 不稳定
"""
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n): # 可以将一次分组的排序放到一个循环中来按顺序处理，不用分组后再在组内各自排。
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -=gap
                else:
                    break
        gap //= 2
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)