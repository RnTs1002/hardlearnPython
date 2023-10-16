#十进制转化为二进制
a = eval(input('请输入十进制数：'))
m = ''
while a > 0:
    m = str(a % 2)
    a = a // 2
print(m[::-1])
#m = bin(a)
#print(m)