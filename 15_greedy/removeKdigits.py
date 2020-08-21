"""
leetcode 402 移掉K位数字
给定一个以字符串表示的非负整数num，移除这个数中的k位数字，使得剩下的数字最小。
num的长度小于10002且>=k
num不会包含任何前导0
思路：运用贪心算法和栈。从高位开始先把最高位append进栈，循环开始，如果下一位比上一位小则上一位出栈，相当于删除一个数字所以k -= 1
如果已经删除K个则不会再删除，如果循环结束并没有删除足够K个则舍弃栈顶（列表后部分）的低位数字保留栈底（列表前部分），
lstrip('0')删除结果字符串的前导0
"""
def removeKdigits(num: str, k: int) ->str:
    numStack = []
    for digit in num:
        while k and numStack and numStack[-1] > digit:
            numStack.pop()
            k -= 1
        
        numStack.append(digit)

    finalStack = numStack[:-k] if k else numStack

    return "".join(finalStack).lstrip('0') or "0"

if __name__ == "__main__":
    num = "10200"
    k = 1
    removed_num = removeKdigits(num, k)
    print(removed_num) # 200
    num = "1432219"
    k = 3
    removed_num = removeKdigits(num, k)
    print(removed_num) # 1219
    num = "10"
    k = 2
    removed_num = removeKdigits(num, k)
    print(removed_num) # 10
