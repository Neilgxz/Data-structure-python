"""
二分查找：二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为 0。
时间复杂度 O(logn)
二分查找的局限性：
    1. 首先，二分查找依赖的是顺序表结构，简单点说就是数组。
    假设使用链表长度为n，二分查找每次都要找到中间点(计算中忽略奇偶数差异):
    第一次查找中间点，需要移动指针n/2次；
    第二次，需要移动指针n/4次；
    第三次需要移动指针n/8次；
    ......
    以此类推，一直到1次为值

    总共指针移动次数(查找次数) = n/2 + n/4 + n/8 + ...+ 1，这显然是个等比数列，根据等比数列求和公式：Sum = n - 1.

    最后算法时间复杂度是：O(n-1)，忽略常数，记为O(n)，时间复杂度和顺序查找时间复杂度相同

    但是稍微思考下，在二分查找的时候，由于要进行多余的运算，严格来说，会比顺序查找时间慢
    2. 其次，二分查找针对的是有序数据。
    3. 再次，数据量太小不适合二分查找。很少的数据顺序遍历已经足够
        如果数据之间的比较比较耗时，不管数据量多少都可以用二分查找
    4. 最后，数据量太大也不适合二分查找。因为需要用数组存储
"""
from typing import List

# 最简单情况：有序数组中不存在重复元素
# 迭代法
def bsearch(nums: List[int], target: int) -> int:

    low, high = 0, len(nums) - 1
    while low <= high:
        # 写成 (low+high)//2 二者之和可能会溢出
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# 递归法
def bsearch_1(nums: List[int], target: int) -> int:
    return bsearch_internally(nums, 0, len(nums)-1, target)

def bsearch_internally(nums: List[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1

    mid = low+int((high-low) >> 2)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bsearch_internally(nums, mid+1, high, target)
    else:
        return bsearch_internally(nums, low, mid-1, target)
# 求一个数的平方根
def squareRoot(a ,precision):
    if a > 1:
        low = 1
        high = a
    else:
        low = a
        high = 1
    while low <= high:
        mid = (low+high)/2.000
        tmp = mid*mid
        if a-tmp <= precision and a-tmp >= precision*0.1:
            return mid
        elif tmp > a:
            high = mid
        else:
            low = mid
    return -1.000

# low 0.5 mid 0.75  high 1 tmp 0.5625 a 0.5
# low 0.5 mid 0.625  high 0.75 tmp 0.390625 a 0.5
# low 0.625 mid 0.6875 high 0.75 tmp 0.47265625 a 0.5
# low 0.6875 mid 0.71875  high 0.75 tmp 0.5166015625 a 0.5
# low 0.6875 mid 0.703125   high 0.71875 tmp 0.494384765625 a 0.5

if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(bsearch(li, 55))
    print(bsearch(li, 100))
    print(bsearch_1(li, 55))
    print(bsearch_1(li, 100))
    num = squareRoot(0.5, 0.000001)
    print(num)
    print("%.6f" % num)