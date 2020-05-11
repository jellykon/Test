class Node():
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList():
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历结点
        cur = self.__head
        # count记录数量
        count = 1
        while cur != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur指向尾节点，但未打印
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            node.next = cur
            self.__head = node
            while cur.next != self.__head:
                cur = cur.next
            cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # node.next = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环推出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != item:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                if cur == self.__head:
                    # 头节点的情况
                    # 找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        self.__head = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找结点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环,cur指向尾结点
        if cur.elem == item:
            return True
        return False
