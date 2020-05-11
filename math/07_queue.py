

class Queue():
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__list.append(item)
        # self.__list.insert(0, item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
        # return self.pop()

    def is_empty(self):
        """判断一个队列是否空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Queue()