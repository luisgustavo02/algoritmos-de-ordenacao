# SELECTION SORT
def selectionSort(v):
    n = len(v)

    for i in range(n):
        minIndex = i

        for j in range(i + 1, n):
            if v[j] < v[minIndex]:
                minIndex = j
        
        v[i], v[minIndex] = v[minIndex], v[i]

    return v
