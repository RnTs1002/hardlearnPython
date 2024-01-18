#牛顿法求解sqrt2
def Square_root_3():
    c = 2
    g = c / 2
    i = 0
    while abs(g*g-c) > 0.00000000001:
        g = (g + c/g)/2
        i = i + 1
    print("%1.4f" % g)

Square_root_3()