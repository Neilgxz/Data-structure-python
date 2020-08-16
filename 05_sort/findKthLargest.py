# Leetcode 215 
import random
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        import random        
        a = self.quick_sort_between(nums, 0, len(nums)-1, k)
        return a
    def quick_sort_between(self, a, low: int, high: int, k: int) -> int:
        if low < high:
            # get a random position as the pivot
            r = random.randint(low, high)
            a[low], a[r] = a[r], a[low]
            m = self.partition(a, low, high)  # a[m] is in final position
            if len(a)-k == m:
                return a[m]
            elif len(a)-k <m:
                return self.quick_sort_between(a, low, m - 1, k)
            else:
                return self.quick_sort_between(a, m + 1, high, k)
        else:
            return a[low]


    def partition(self, a, low: int, high: int):
        pivot, j = a[low], low
        for i in range(low + 1, high + 1):
            if a[i] <= pivot:
                # 只有小于等于pivot时j才会动，所以j一直指向小于等于pivot的最后一个位置。
                j += 1
                a[j], a[i] = a[i], a[j]  # swap
        a[low], a[j] = a[j], a[low]
        return j
if __name__ == "__main__":
    test1= Solution()
    nums = [1]
    k = 1 
    print(test1.findKthLargest(nums, k)) 
    