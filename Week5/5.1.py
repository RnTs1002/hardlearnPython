#判断输入a是否为质数
a =int(input("输入一个数："))
flag = True
for i in range(2, a):
    if a % i == 0:
        flag = False
        break

if flag:
    print(a, "是质数")
else:
    print(a, "不是质数")
