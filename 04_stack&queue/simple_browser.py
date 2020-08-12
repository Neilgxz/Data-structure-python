"""
    a simple browser realize
    Author: zhenchao.zhu
    解答：我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X，当点击后退按钮时，再依次从栈 X 中出栈，
    并将出栈的数据依次放入栈 Y。当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。当栈 Y 中没有数据，
    那就说明没有页面可以点击前进按钮浏览了。
    打开新的页面压入栈X。应当同时清空栈Y，不能前进得到之前后退到栈Y的界面。
"""

import sys
# 引用当前文件夹下的single_linked_list
sys.path.append('linked_stack.py')
from linked_stack import LinkedStack

class NewLinkedStack(LinkedStack):

    def is_empty(self):
        return not self._top


class Browser():

    def __init__(self):
        self.forward_stack = NewLinkedStack() # 栈X，新页面压入，以及前进压入的栈
        self.back_stack = NewLinkedStack() # 栈Y，后退压入的栈

    def can_forward(self):
        if self.back_stack.is_empty(): # 栈Y空，没有页面可以前进。
            return False
        return True

    def can_back(self):
        if self.forward_stack.is_empty(): # 栈X空，没有页面可以后退。
            return False
        return True

    def open(self, url):
        print("Open new url %s" % url, end="\n")
        # 打开页面压入栈X。应当同时清空栈Y，不能前进得到之前后退到栈Y的界面。
        self.forward_stack.push(url)
        self.back_stack = NewLinkedStack()

    def back(self):
        # 栈X为空，没有页面可以后退
        if self.forward_stack.is_empty():
            return None
        # 栈X不为空，取出最上面的页面，压入栈Y
        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print("back to %s" % top, end="\n")

    def forward(self):
        # 栈Y为空，没有页面可以前进
        if self.back_stack.is_empty():
            return
        # 栈Y不为空，取出最上面的页面，压入栈X
        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print("forward to %s" % top, end="\n")


if __name__ == '__main__':

    browser = Browser()
    print(browser.back())
    browser.open('a')
    browser.open('b')
    browser.open('c')
    browser.back()
    browser.back()
    browser.open('d')
    print(browser.forward())
    browser.back()
    browser.forward()
