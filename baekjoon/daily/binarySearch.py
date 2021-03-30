def binary_search(lst, N, K):
    lo, hi = 0, N-1
    while lo <= hi:
        mid = (lo+hi) // 2
        if lst[mid] == K: return True
        if lst[mid] > K: hi = mid-1
        else: lo = mid+1
    return False
