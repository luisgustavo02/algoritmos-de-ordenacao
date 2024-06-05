# TIM SORT
def timSort(v, MIN_RUN = 32):
    def insertion_sort(array, left, right):
        for i in range(left + 1, right + 1):
            key = array[i]
            j = i - 1

            while j >= left and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            
            array[j + 1] = key
    
    def merge(array, le, mi, ri):
        len1, len2 = mi - le + 1, ri - mi
        left, right = [], []

        for i in range(len1):
            left.append(array[le + i])
        for i in range(len2):
            right.append(array[mi + i + 1])
        
        i, j, k, = 0, 0, le

        while i < len1 and j < len2:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            
            else:
                array[k] = right[j]
                j += 1
            
            k += 1
        
        while i < len1:
            array[k] = left[i]
            k += 1
            i += 1
        
        while j < len2:
            array[k] = right[j]
            k += 1
            j += 1
    
    n = len(v)

    for i in range(0, n, MIN_RUN):
        insertion_sort(v, i, min((i + MIN_RUN - 1), n - 1))
    
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            if mid < end:
                merge(v, start, mid, end)
        size *= 2
    
    return v
