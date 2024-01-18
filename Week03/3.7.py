#最大公约数/辗转相除法
def fun(a,b):
    x = a % b
    while(x!=0):
        a = b
        b = x
        x = a % b
    return b
a = int(input())
b = int(input())
print(fun(a,b))