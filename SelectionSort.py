
#selection sort
def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [7, 6, 5, 4, 2, 9]
selection_sort = selection(arr)
print("Sorted Array Using Selection Sort:", selection_sort)
