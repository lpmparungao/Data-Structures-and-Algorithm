def selection_sort(arr):

    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [5, 2, 9, 4, 6]
print("Sorted array is:")
selection_sort(arr)
print(arr)