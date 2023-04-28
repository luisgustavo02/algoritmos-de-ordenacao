def bubbleSort(v):
    for i in range(0, n):
        for j in range(i, n-1):
            if v[j] > v[j+1]:
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux
                
