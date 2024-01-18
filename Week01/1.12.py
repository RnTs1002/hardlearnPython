#二分逼近法

def bsearch(l,r):
    while r - l > 1e-8:
        mid = (l + r) / 2
        if mid ** 3 < n:
            l = mid
        else:
            r = mid
    print('{:.6}'.format(l))

n = float(input())
r = n
bsearch(0,r)