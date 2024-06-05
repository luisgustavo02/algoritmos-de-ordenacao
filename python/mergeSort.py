# MERGE SORT
def mergeSort(v):
    def merge(left, right):
        sortedArray = []
        leftIndex, rightIndex = 0, 0

        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                sortedArray.append(left[leftIndex])
                leftIndex += 1
            else:
                sortedArray.append(right[rightIndex])
                rightIndex += 1

        sortedArray.extend(left[leftIndex:])
        sortedArray.extend(right[rightIndex:])

        return sortedArray

    if len(v) <= 1:
        return v

    middle = len(v) // 2
    left = mergeSort(v[:middle])
    right = mergeSort(v[middle:])

    return merge(left, right)
