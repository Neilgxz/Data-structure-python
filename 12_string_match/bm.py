#!/usr/bin/python
# -*- coding: UTF-8 -*-

SIZE = 256


def bm(main, pattern):
    """
    BM算法
    匹配规则：
    1. 坏字符规则
    2. 好后缀规则
    :param main: 主串
    :param pattern: 模式串
    :return: 找到的匹配子串的起始下标
    """
    assert type(main) is str and type(pattern) is str
    n, m = len(main), len(pattern)

    if n <= m:
        return 0 if main == pattern else -1

    # bc
    bc = [-1] * SIZE
    generate_bc(pattern, m, bc)

    # gs
    suffix = [-1] * m
    prefix = [False] * m
    generate_gs(pattern, m, suffix, prefix)
    
    i = 0
    while i < n-m+1:
        j = m - 1
        # 得到坏字符下标j
        while j >= 0:
            if main[i+j] != pattern[j]:
                break
            else:
                j -= 1

        # pattern整个已被匹配，返回
        if j == -1:
            return i

        # 1. bc规则计算后移位数
        x = j - bc[ord(main[i+j])]

        # 2. gs规则计算后移位数
        y = 0
        if j != m - 1:    # 存在gs
            y = move_by_gs(j, m, suffix, prefix)

        i += max(x, y) # 取两个规则结果的最大值

    return -1


def generate_bc(pattern, m, bc):
    """
    生成坏字符哈希表
    :param pattern: 模式串
    :param m: 模式串长度
    :param bc: 模式串中字符的哈希表
    :return: 模式串中字符的哈希表
    """
    for i in range(m):
        # 采用模式串中的字符的ASCII码值作为下标，bc数组值为这个字符在模式串中最后一次出现的下标 0~m-1
        bc[ord(pattern[i])] = i


def generate_gs(pattern, m, suffix, prefix):
    """
    好后缀预处理
    :param pattern: 模式串
    :param m: 模式串长度
    :param suffix: suffix[k] = i 若i!=-1表示模式串长度为K的后缀与模式串中i为起始下标的长度为k的子串相同
    :param prefix: prefix[k] = True 表示模式串长度为K的后缀 与 模式串中长度为k的前缀子串相同
    :return: 模式串的suffix和prefix数组
    """
    for i in range(m-1): 
        k = 0   # pattern[:i+1]和pattern的公共后缀长度
        for j in range(i, -1, -1):
            if pattern[j] == pattern[m-1-k]:
                k += 1
                suffix[k] = j
                if j == 0:
                    prefix[k] = True
            else:
                break
    # 例如模式串 c a b c a b
    # i = 0, j = 0, k = 0 比较pattern[0] 和pattern[5]  c!=b
    # i = 1, j = 1, k = 0 比较pattern[1] 和pattern[5]  a!=b
    # i = 1, j = 0, k = 0 比较pattern[0] 和pattern[5]  c!=b 
    # i = 2, j = 2, k = 0 比较pattern[2] 和pattern[5]  b==b k = 1, suffix[1] = 2 长度为1的模式串后缀 找到的第一个匹配子串的起始下标为2 
    # i = 2, j = 1, k = 1 比较pattern[1] 和pattern[4]  a==a k = 2, suffix[2] = 1 长度为2的模式串后缀 找到的第一个匹配子串的起始下标为1 
    # i = 2, j = 0, k = 2 比较pattern[0] 和pattern[3]  c==c k = 3, suffix[3] = 0 长度为3的模式串后缀 找到的第一个匹配子串的起始下标为0 prefix[3] = True
    # .....
 

def move_by_gs(j, m, suffix, prefix):
    """
    通过好后缀计算移动值
    需要处理三种情况：
    1. 整个好后缀在pattern仍能找到
    2. 好后缀里存在 *后缀子串* 能和pattern的 *前缀* 匹配
    3. 其他
    :param j: 最后一个坏字符的下标
    :param m: 模式串长度
    :param suffix: suffix[k] = i 若i!=-1表示模式串长度为K的后缀与模式串中i为起始下标的长度为k的子串相同
    :param prefix: prefix[k] = True 表示模式串长度为K的后缀 与 模式串中长度为k的前缀子串相同
    :return: 好后缀规则下的向后移动的长度
    """
    k = m - 1 - j           # j指向从后往前的第一个坏字符，k是此次匹配的好后缀的长度

    if suffix[k] != -1:             # 1. 整个好后缀在pattern剩余字符中仍有出现
        return j - suffix[k] + 1
    else:
        for r in range(j+2, m):     # 2. 后缀子串从长到短搜索
            if prefix[m-r]:
                return r
        return m                    # 3. 其他情况


if __name__ == '__main__':
    print('--- search ---')
    m_str = 'dfasdeeeetewtweyyyhtruuueyytewtweyyhtrhrth'
    p_str = 'eyytewtweyy'
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[bm] result:', bm(m_str, p_str))
