#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):               
        for j in range(n - i - 1):        
            if arr[j] > arr[j + 1]:      
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr                           



arr = [7, 6, 5, 4, 2, 9]
sorted_arr = bubble_sort(arr)
print("Sorted array using Bubble sort:", sorted_arr)