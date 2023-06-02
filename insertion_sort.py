def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Ví dụ sử dụng thuật toán sắp xếp chèn
my_list = [64, 25, 12, 22, 11]
sorted_list = insertion_sort(my_list)
print("Danh sách đã được sắp xếp:", sorted_list)
