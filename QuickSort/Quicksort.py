def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Contoh penggunaan
arr = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_arr = quick_sort(arr)
print("Array sebelum pengurutan:", arr)
print("Array setelah pengurutan:", sorted_arr)