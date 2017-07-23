
def multiply(a, b):
    i = 0
    while i < len(a):
        a[i] = a[i] * b
        i += 1
    return a


a = [2,4,10,16]
b = multiply(a, 5)
print b
