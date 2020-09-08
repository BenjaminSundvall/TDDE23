# Fast version
def choose(n, k):
    k = min(k, n-k)                             # optimize for large k:s

    if k==0 or k==n:
        return 1
    else:
        return (n * choose(n-1, k-1) // k)      # n choose k is equal to n/k * n-1 choose k-1
