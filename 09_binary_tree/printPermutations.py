"""
    先交换 数组第一个和最后一个数，转化为前n-1个数全排列的问题。
    当这些处理完，在把第一个数字换回来。把第二个数字换到最后，仍转化为n-1个数全排列的问题。
    相当于n个n-1个数全排列的问题。
"""
def printPermutations(nums, k):
    if k == 0:
        return
    if k == 1:
        for i in nums:
            print(i, end=" ")
        print(" ")
    for i in range(k):
        nums[i], nums[k-1] = nums[k-1], nums[i]
        printPermutations(nums, k-1)
        nums[i], nums[k-1] = nums[k-1], nums[i]

if __name__ == "__main__":
    nums = [1, 2, 3]
    k = len(nums)
    printPermutations(nums,k)
    