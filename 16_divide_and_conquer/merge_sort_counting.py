#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
编程求出一组数据的逆序对个数：
利用分治算法，归并排序
"""
inversion_num = 0


def merge_sort_counting(nums, start, end):
    if start >= end:
        return

    mid = (start + end)//2
    merge_sort_counting(nums, start, mid)
    merge_sort_counting(nums, mid+1, end)
    merge(nums, start, mid, end)


def merge(nums, start, mid, end):
    global inversion_num
    i = start
    j = mid+1
    tmp = []
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            # nums[j]中的元素原本在nums[i]的元素的后边，但是数值却比nums[i]中的一些要小，排序时被放到前面来，所以可以累加逆序度
            inversion_num += mid - i + 1
            tmp.append(nums[j])
            j += 1

    while i <= mid:

        tmp.append(nums[i])
        i += 1

    while j <= end:

        tmp.append(nums[j])
        j += 1

    nums[start: end+1] = tmp


if __name__ == '__main__':
    print('--- count inversion number using merge sort ---')
    nums = [5, 0, 4, 2, 3, 1, 3, 3, 3, 6, 8, 7]
    print('nums  : {}'.format(nums))
    merge_sort_counting(nums, 0, len(nums)-1)
    print('sorted: {}'.format(nums))
    print('inversion number: {}'.format(inversion_num))
