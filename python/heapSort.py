# HEAP SORT
def heapSort(v):
    def heapify(array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[left] > array[largest]:
            largest = left

        if right < n and array[right] > array[largest]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)
    
    n = len(v)

    for i in range(n // 2 - 1, -1, -1):
        heapify(v, n, i)

    for i in range(n - 1, 0, -1):
        v[i], v[0] = v[0], v[i]  # Troca
        heapify(v, i, 0)
    
    return v
