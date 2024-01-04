def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan indeks jika target ditemukan
    return -1  # Mengembalikan -1 jika target tidak ditemukan

# Contoh penggunaan
arr = [2, 5, 8, 12, 16, 23, 38, 45, 50]
target = 16

result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} ditemukan pada indeks {result}.")
else:
    print(f"Target {target} tidak ditemukan dalam array.")
