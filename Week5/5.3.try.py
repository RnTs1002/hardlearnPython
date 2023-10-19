# 直接插入排序
import numpy as np


def insert_sort(data: list):
    init = np.array([0])  # 将数组第一个位置留空，或者作为哨兵
    unsort = np.append(init, data)
    for i in range(2, unsort.size):
        if unsort[i] < unsort[i - 1]:
            unsort[0] = unsort[i]  # 将待插入的记录暂存到监视哨
            unsort[i] = unsort[i - 1]  # i-1位置已经比较过了，可以向后移动
            for j in range(i - 2, -1, -1):  # 从后向前寻找插入位置，比较区间: [i-2, ..., 0]
                if unsort[0] < unsort[j]:
                    unsort[j + 1] = unsort[j]  # 比监视哨大的元素都向后移一位，腾出插入空间
                else:
                    unsort[j + 1] = unsort[0]  # 完成本轮插入
                    break
    return unsort[1:]


def test_1():
    a = [1, 45, 76,
         89, 84, 23,
         11, 32, 44]
    print(f"排序前: {a}")
    print(f"排序后: {insert_sort(a)}")


def test_2():
    b = [i for i in range(10, 0, -1)]
    print(f"排序前: {b}")
    print(f"排序后: {insert_sort(b)}")


if __name__ == '__main__':
    test_2()