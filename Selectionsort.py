a = [16,10,-1,369,5]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
