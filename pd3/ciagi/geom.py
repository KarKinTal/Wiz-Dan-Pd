def n_ty_wyraz_a1 (a1, n, q):

    return a1 * (q**(n-1))

def n_ty_wyraz_ak (ak, n, k, q):

    return ak * (q**(n-k))

def suma (a1, q, n):
    if q == 1:
        return a1 * n
    else:
        return a1 * (1 - q**n)/(1 - q)
