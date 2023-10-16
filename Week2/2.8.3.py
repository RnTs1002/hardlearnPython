#黎曼和（定积分）
import math
N = 1000000
def Riemann_pi(N):
    pi = 0
    fin_sum = 0
    for i in range(0,N):
        mid = (i+0.5)/N
        fin_sum += 1/N * math.sqrt(1 - mid**2)
    pi = fin_sum*4
    print(pi)

Riemann_pi(N)