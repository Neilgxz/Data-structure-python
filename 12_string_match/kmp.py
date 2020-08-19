#!/usr/bin/python
# -*- coding: UTF-8 -*-


def kmp(main, pattern):
    """
    kmp字符串匹配
    :param main:
    :param pattern:
    :return:
    """
    assert type(main) is str and type(pattern) is str

    n, m = len(main), len(pattern)

    if m == 0:
        return 0
    if n <= m:
        return 0 if main == pattern else -1

    # 求解next数组
    next = get_next(pattern)
    # 其实j记录了 已经有多少位连续匹配成功
    j = 0
    for i in range(n): 
        # 在pattern[:j]中，从长到短递归去找最长的和后缀子串匹配的前缀字串
        while j > 0 and main[i] != pattern[j]:
            # 遇到坏字符，则模式串0~j-1为好前缀，计算next[j-1]得到最长的可以与后缀子串匹配的前缀字串的结尾下标
            # 将j移动到这个最长匹配前缀的后一个位置，继续比较
            j = next[j-1] + 1   
        # 结束循环，j=0 或者 main[i] == pattern[j]
        if main[i] == pattern[j]:
            if j == m-1: # 对比到模式串的最后一位，全部匹配
                return i-m+1
            else: 
                j += 1
        # 一次循环结束，如果始终没有 main[i] == pattern[j]，i += 1 从下一位开始从模式串头开始比较。
        # 如果j += 1 if结束后i也会+1 继续对比下一位 
    return -1


def get_next(pattern):
    """
    next数组生成

    注意：
    理解的难点在于next[i]根据next[0], next[1]…… next[i-1]的求解
    next[i]的值依赖于前面的next数组的值，求解思路：
    1. 首先取出前一个最长的匹配的前缀子串，其下标就是next[i-1]
    2. 对比下一个字符，如果匹配，直接赋值next[i]为next[i-1]+1，因为i-1的时候已经是最长
    *3. 如果不匹配，需要递归去找次长的匹配的前缀子串，这里难理解的就是递归地方式，next[i-1]
        是i-1的最长匹配前缀子串的下标结尾，则 *next[next[i-1]]* 是其次长匹配前缀子串的下标
        结尾
    *4. 递归的出口，就是在次长前缀子串的下一个字符和当前匹配 或 遇到-1，遇到-1则说明没找到任
        何匹配的前缀子串，这时需要找pattern的第一个字符对比

    ps: next[m-1]的数值其实没有任何意义，求解时可以不理。网上也有将next数组往右平移的做法。
    :param pattern:
    :return:
    """
    m = len(pattern)
    next = [-1] * m

    next[0] = -1 # 好前缀只有一个元素，没有前缀和后缀

    # for i in range(1, m):
    for i in range(1, m-1):
        j = next[i-1]       # 取i-1时匹配到的最长前缀子串
        while j != -1 and pattern[j+1] != pattern[i]:
            j = next[j]     # 次长的前缀子串的结尾下标，即是next[next[i-1]]

        # 根据上面跳出while的条件，当j=-1时，需要比较pattern[0]和当前字符
        # 如果j!=-1，则pattern[j+1]和pattern[i]一定是相等的
        if pattern[j+1] == pattern[i]:  # 如果接下来的字符也是匹配的，那i的最长前缀子串下标是next[i-1]+1
            j += 1
        next[i] = j

    return next


if __name__ == '__main__':
    m_str = "aabbbbaaabbababbabbbabaaabb"
    p_str = "abbabbbabaa"

    print('--- search ---')
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[kmp] result:', kmp(m_str, p_str))
