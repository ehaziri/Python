
v = [4, 5, 1, 3, 2]


for k in range(0, 5):
    for i in range(0,4):

        j = i+1

        if(v[i] > v[j]):
            temp = v[i]
            v[i] = v[j]
            v[j] = temp

print v
