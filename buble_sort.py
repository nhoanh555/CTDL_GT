def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Bỏ qua i phần tử cuối cùng đã được sắp xếp
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ví dụ sử dụng thuật toán sắp xếp nổi bọt
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print("Danh sách đã được sắp xếp:", sorted_list)
