list = []
def Solution(n):
    if n == 1 or n == 2:
        list.append(n)
    else:
        q = n // 3
        r = n % 3
        if r == 0:
            for i in range(q):
                list.append(3)
        if r == 1:
            list.append(2,2)
            for i in range(q-1):
                list.append(3)
        if r == 2:
            list.append(2)
            for i in range(q):
                list.append(3)
    print(list)

n = int(input("输入n："))
Solution(n)