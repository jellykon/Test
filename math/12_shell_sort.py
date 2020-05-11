def shell_sort(alist):
    """希尔排序"""
    # n=9
    n = len(alist)
    # gap = 4
    gap = n // 2

    # i = gap
    # for i in range(gap, n)
    #       i = [gap, gap+1, gap+2, ... n-1
    #       while:
    #         if alist[i] < alist[i=gap]:
    #             alist[i], alist[i-gap] = alist[i-gap], alist[i]

    # gap变化到0之前，插入算法执行的次数
    while gap >= 0:
        # 插入算法，与普通的插入算法区别就是gap步长
        for j in range(gap, n):
            # j = [gap, gap+1, gap+2, ..., n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
         # 缩短gap步长
        gap //= 2


if __name__ == "__main__":
    alist = [11, 15, 1, 19, 20, 17, 29, 12, 9, 19]
    print(alist)
    shell_sort(alist)
    print(alist)