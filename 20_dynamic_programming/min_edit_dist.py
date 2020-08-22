"""
    Author: Wenru Dong
    量化两个字符串之间的相似程度：编辑距离（Edit Distance）
    将一个字符串转化成另一个字符串，需要的最少编辑操作次数（比如增加一个字符、删除一个字符、替换一个字符）。编辑距离越大，说明两个字符串的相似程度越小；
    相反，编辑距离就越小，说明两个字符串的相似程度越大。对于两个完全相同的字符串来说，编辑距离就是 0。
"""

def levenshtein_dp(s: str, t: str) -> int:
    """
     莱文斯坦距离：增加，删除，替换字符
     莱文斯坦距离的大小，表示两个字符串差异的大小
     如果 a[i]与 b[j]匹配，我们递归考察 a[i+1]和 b[j+1]
     如果 a[i]与 b[j]不匹配，那我们有多种处理方式可选：
        可以删除 a[i]，然后递归考察 a[i+1]和 b[j]；
        可以删除 b[j]，然后递归考察 a[i]和 b[j+1]；
        可以在 a[i]前面添加一个跟 b[j]相同的字符，然后递归考察 a[i]和 b[j+1];
        可以在 b[j]前面添加一个跟 a[i]相同的字符，然后递归考察 a[i+1]和 b[j]；
        可以将 a[i]替换成 b[j]，或者将 b[j]替换成 a[i]，然后递归考察 a[i+1]和 b[j+1]。
    我们只需要保留编辑次数最小的方法，(i,j)状态可以从(i-1, j)，(i, j-1)，(i-1, j-1) 三个状态中的任意一个转移过来。
    """
    m, n = len(s), len(t)
    table = [[0] * (n) for _ in range(m)] # m行n列

    for i in range(n):
        # 初始化第0行，table[0][i]表示s串的第0个字符与t串前i个字符的编辑距离
        if s[0] == t[i]:
            table[0][i] = i - 0
        elif i != 0:
            table[0][i] = table[0][i - 1] + 1
        else:
            table[0][i] = 1

    for i in range(m):
        # 初始化第0列，table[i][0]表示t串的第0个字符与s串前i个字符的编辑距离
        if s[i] == t[0]:
            table[i][0] = i - 0
        elif i != 0:
            table[i][0] = table[i - 1][0] + 1
        else:
            table[i][0] = 1
    # 三种情况：
    # 1. table[i - 1][j] s串的0~i-1个字符与t串的0~j个字符的编辑距离已知，在此基础上table[i][j]的S串多了一个字符，如果想让两串相互转化，则一定会有一次编辑所以+1
    # 2. table[i][j - 1] s串的0~i个字符与t串的前0~j-1个字符的编辑距离已知，在此基础上table[i][j]的t串多了一个字符，如果想让两串相互转化，则一定会有一次编辑所以+1  
    # 3. table[i - 1][j - 1] s串的0~i-1个字符与t串的0~j-1个字符的编辑距离已知，在此基础上table[i][j]的s和t串都多了一个字符
    #    如果多出来的字符相同，那么就不用编辑，如果多出来的字符不同，则需要进行一次编辑所以+ int(s[i] != t[j])
        for j in range(1, n):
            table[i][j] = min(1 + table[i - 1][j], 1 + table[i][j - 1], int(s[i] != t[j]) + table[i - 1][j - 1])

    print(table)
    return table[-1][-1]

# 最长公共子串长度：增加，删除字符
# 最长公共子串的大小，表示两个字符串相似程度的大小
def common_substring_dp(s: str, t: str) -> int:
    """
    如果 a[i]与 b[j]互相匹配，我们将最大公共子串长度加一，并且继续考察 a[i+1]和 b[j+1]。
    如果 a[i]与 b[j]不匹配，最长公共子串长度不变，这个时候，有两个不同的决策路线：
        删除 a[i]，或者在 b[j]前面加上一个字符 a[i]，然后继续考察 a[i+1]和 b[j]；
        删除 b[j]，或者在 a[i]前面加上一个字符 b[j]，然后继续考察 a[i]和 b[j+1]。
    table[i][j] 表示s串从0~i字符与t串0~j个字符的最长公共长度
    """
    m, n = len(s), len(t)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = max(table[i - 1][j], table[i][j - 1], int(s[i - 1] == t[j - 1]) + table[i - 1][j - 1])
    return table[-1][-1]


if __name__ == "__main__":
    s = "mitcmu"
    t = "mtacnu"

    print(levenshtein_dp(s, t))
    print(common_substring_dp(s, t))

    s = "kitten"
    t = "sitting"

    print(levenshtein_dp(s, t))
    print(common_substring_dp(s, t))

    s = "flaw"
    t = "lawn"

    print(levenshtein_dp(s, t))
    print(common_substring_dp(s, t))