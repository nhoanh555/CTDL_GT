def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n-1)

n = int(input("Nhập số nguyên dương n: "))
print("Giai thừa của", n, "là", giaithua(n))
