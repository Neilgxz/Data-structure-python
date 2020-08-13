"""
    Author: Wenru
    Fix: nzjia
    二分查找的变体
"""
from typing import List

def bsearch_left(nums: List[int], target: int) -> int:
    """Binary search of the index of the first element
    equal to a given target in the ascending sorted array.
    If not found, return -1.
    查找第一个值等于给定值的元素。
    存在重复元素
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            # 相等时，如果mid是第一个元素或者他的前一个元素不是target。那么他就是第一个值等于给定值的元素
            if mid == 0 or a[mid-1] != target:
                return mid
            else:
                high = mid - 1
    return -1

def bsearch_right(nums: List[int], target: int) -> int:
    """Binary search of the index of the last element
    equal to a given target in the ascending sorted array.
    If not found, return -1.
    查找最后一个值等于给定值的元素
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            # 相等时，如果mid是最后一个元素或者他的后一个元素不是target。那么他就是最后一个值等于给定值的元素
            if mid == len(nums) - 1 or a[mid+1] != target:
                return mid
            else:
                low = mid + 1
    return -1

def bsearch_left_not_less(nums: List[int], target: int) -> int:
    """Binary search of the index of the first element
    not less than a given target in the ascending sorted array.
    If not found, return -1.
    查找第一个大于等于给定值的元素。
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            # nums[mid]大于等于target时，如果mid是第一个元素或者他的前一个元素小于target。那么他就是最后一个值大于等于给定值的元素
            if mid == 0 or a[mid-1] < target:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1

def bsearch_right_not_greater(nums: List[int], target: int) -> int:
    """Binary search of the index of the last element
    not greater than a given target in the ascending sorted array.
    If not found, return -1.
    查找最后一个小于等于给定值的元素
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            # nums[mid]大于等于target时，如果mid是第一个元素或者他的前一个元素小于target。那么他就是最后一个值大于等于给定值的元素
            if mid == len(nums) - 1 or a[mid + 1] > target:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        leetcode 33
        假设按照升序排序的数组在预先未知的某个点上进行了旋转。
        ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
        搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
        你可以假设数组中不存在重复的元素。
        你的算法时间复杂度必须是 O(log n) 级别。
        示例 1:
        输入: nums = [4,5,6,7,0,1,2], target = 0
        输出: 4
        分析：运用二分查找。原先的有序数组经过旋转分成两个升序的有序数组。
        如果 nums[0] <= nums[mid]: 说明从0到mid一定是升序。那么如果target在其中 则二分区间变为 [0,mid-1]，不在其中则 [mid+1,n-1]
        如果 nums[0] > nums[mid]: 说明从mid到n-1一定是升序。那么如果target在其中 则二分区间变为 [mid+1,n-1]，不在其中则 [0,mid-1]
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    a = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22]

    print(bsearch_left(a, 0) == -1)
    print(bsearch_left(a, 7) == 6)
    print(bsearch_left(a, 30) == -1)

    print(bsearch_right(a, 0) == -1)
    print(bsearch_right(a, 7) == 9)
    print(bsearch_right(a, 30) == -1)

    print(bsearch_left_not_less(a, 0) == 0)
    print(bsearch_left_not_less(a, 5) == 5)
    print(bsearch_left_not_less(a, 30) == -1)

    print(bsearch_right_not_greater(a, 0) == -1)
    print(bsearch_right_not_greater(a, 6) == 5)
    print(bsearch_right_not_greater(a, 30) == 11)

    nums = [4,5,6,7,0,1,2]
    target = 0
    b = Solution()
    print(b.search(nums, target)) # 4
    target = 3
    print(b.search(nums, target)) # -1