#牛顿迭代法求三次方根
def Cubic_root():
    n = 9
    k = n / 3
    while abs(k*k*k - n) > 0.00000000001:
        k2 = k * k
        k3 = k2 * k
        k = k - (k3 - n) / (3 * k2)
    print(k)

Cubic_root()