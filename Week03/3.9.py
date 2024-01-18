def multiply(A):
    n = len(A)
    C = [1]*len(A)
    D = [1]*len(A)
    B = [1]*len(A)
    for i in range(1,n):
        C[i] = C[i-1]*A[i-1]
    for j in (range(0,n-1))[::-1]:
        D[j] = D[j+1]*A[j+1]

    for k in range(0,n):
        B[k] = C[k]*D[k]
    print(B)

A = [1, 1, 1, 1]
multiply(A)