def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)

# Ví dụ sử dụng thuật toán sắp xếp nhanh
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(my_list)
print("Danh sách đã được sắp xếp:", sorted_list)
