#牛顿法求解sqrt2
#改变c值不影响结果
def Square_root_4():
    c = 2
    g = c
    i = 0
    while abs(g*g-c) > 0.00000000001:
        g = (g + c/g)/2
        i = i + 1
    print("%1.4f" % g)

Square_root_4()