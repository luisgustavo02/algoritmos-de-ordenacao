# BUBBLE SORT
def bubbleSort(v):
    for i in range(0, len(v)):
        for j in range(i, len(v)):
            if v[j] < v[i]:
                v[j], v[i] = v[i], v[j]
    
    return v
