

class Stack():
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        return self.__list.append(item)

    def peek(self):
        """返回栈顶元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == '__main__':
    s = Stack()