# QUICK SORT
def quickSort(v):
    if len(v) <= 1:
        return v
    else:
        pivot = v[len(v) // 2]
        left = [i for i in v if i < pivot]
        middle = [i for i in v if i == pivot]
        right = [i for i in v if i > pivot]

        return quickSort(left) + middle + quickSort(right)
