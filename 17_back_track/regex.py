#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
正则表达式：假设正则表达式中只包含“*”和“?”这两种通配符，如何用回溯算法，判断一个给定的文本，能否跟给定的正则表达式匹配？
当是非通配符时，我们就直接跟文本的字符进行匹配，如果相同，则继续往下处理；如果不同，则回溯。
如果遇到特殊字符的时候，我们就有多种处理方式了，也就是所谓的岔路口，
比如“*”有多种匹配方案，可以匹配任意个文本串中的字符，我们就先随意的选择一种匹配方案，然后继续考察剩下的字符。
如果中途发现无法继续匹配下去了，我们就回到这个岔路口，重新选择一种匹配方案，然后再继续匹配剩下的字符。
"""
is_match = False


def rmatch(r_idx: int, m_idx: int, regex: str, main: str):
    global is_match
    if is_match:
        return

    if r_idx >= len(regex):     # 正则串全部匹配好了
        is_match = True
        return

    if m_idx >= len(main) and r_idx < len(regex):   # 正则串没匹配完，但是主串已经没得匹配了
        is_match = False
        return

    if regex[r_idx] == '*':     # * 匹配1个或多个任意字符，递归搜索每一种情况
        for i in range(m_idx, len(main)):
            rmatch(r_idx+1, i+1, regex, main)
    elif regex[r_idx] == '?':   # ? 匹配0个或1个任意字符，两种情况
        rmatch(r_idx+1, m_idx+1, regex, main)
        rmatch(r_idx+1, m_idx, regex, main)
    else:                       # 非特殊字符需要精确匹配
        if regex[r_idx] == main[m_idx]:
            rmatch(r_idx+1, m_idx+1, regex, main)


if __name__ == '__main__':
    regex = 'ab*eee?d'
    main = 'abcdsadfkjlekjoiwjiojieeecd'
    rmatch(0, 0, regex, main)
    print(is_match)
