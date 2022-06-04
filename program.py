a=[10,20,30,5,2,50]
for i in a:
    j=a.index(i)
    while j>0:
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
            j=j-1
        else:
            break
print(a)
