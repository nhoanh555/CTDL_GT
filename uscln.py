def uscln(a, b):
    if b == 0:
        return a
    else:
        return uscln(b, a % b)
    
result = uscln(60, 48)
print(result)

