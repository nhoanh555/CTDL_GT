def hanoi(n, start, end, middle):
    if n == 1:
        print("Đổi đĩa 1 từ cột", start, "tới cột", end)
        return
    hanoi(n - 1, start, middle, end)
    print("Đổi đĩa", n, "từ cột", start, "tới cột", end)
    hanoi(n - 1, middle, end, start)

n = int(input("Nhập số lượng đĩa: "))
hanoi(n, 'A', 'C', 'B')
