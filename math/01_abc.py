from timeit import Timer


def t1():
    li = []
    for i in range(10000):
        li.append(i)


def t2():
    li = []
    for i in range(10000):
        li += [i]


def t3():
    li = [i for i in range(10000)]


def t4():
    li = list(range(10000))


def t5():
    for i in range(10000):
        li = []
        li.extend([i])


timer1 = Timer("t1()", "from __main__ import t1")
print("append:", timer1.timeit(1000))


timer2 = Timer("t2()", "from __main__ import t1")
print("+:", timer1.timeit(1000))


timer3 = Timer("t3()", "from __main__ import t1")
print("[i for i in range]:", timer1.timeit(1000))


timer4 = Timer("t4()", "from __main__ import t1")
print("list(range())", timer1.timeit(1000))


timer5 = Timer("t5()", "from __main__ import t1")
print("extend", timer1.timeit(1000))
