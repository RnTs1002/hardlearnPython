#蒙特卡洛法
import numpy as np
#import matplotlib.pyplot as plt
def monte_carlo_pi(N):
    number_inside = 0
    points_inside = [[], []]
    points_outside = [[], []]
    current_pi = []
    i = 0
    count = 0
    # n 为传入的总点数量
    while i < N:
        # 随机产生x,y坐标
        x, y = np.random.uniform(-1, 1, 2)
        # 如果x平方 + y平方 < 1，说明在圆内
        if (pow(x, 2) + pow(y, 2)) < 1:
            number_inside += 1
            points_inside[0].append(x)
            points_inside[1].append(y)
        else:
            points_outside[0].append(x)
            points_outside[1].append(y)
        current_pi.append(4 * number_inside /(i+1))
        i += 1
    # π的值为：4 * （落在圆内的点/总的点）
    return (points_inside, points_outside, current_pi)