

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(ls):
    if ls is None:
        return None
    head = ListNode(ls[0])
    cur = head
    ls = ls[1:]
    for i in ls:
        cur.next = ListNode(i)
        cur = cur.next
    cur.next = None
    return head


def printLinkList(head):
    cur = head
    while cur:
        print("%s->" % cur.val, end="")
        cur = cur.next
    print("None")




def getIntersectionNode(headA, headB):
    hasht = {}
    print(headA)
    print(headB)
    while headA is not None:
        hasht[headA], headA = headA, headA.next
    while headB is not None:
        if headB in hasht:
            print(headB)
        else:
            headB = headB.next
    return None


if __name__ == '__main__':
    head1 = createLinkedList([4,1,8,4,5])
    printLinkList(head1)
    head2 = createLinkedList([5,0,1,8,4,5])
    getIntersectionNode(head1, head2)

