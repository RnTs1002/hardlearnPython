#“笨办法”求解sqrt2
def Sqare_root_1():
    c = 2
    i = 0
    g = 0
    for j in range(0, c + 1):
        if j * j > c and g == 0:
            g = j - 1
        while abs(g * g - c) > 0.0001:
            g += 0.00001
            i = i + 1
        break
    print(format(g,'.4f'))

Sqare_root_1()